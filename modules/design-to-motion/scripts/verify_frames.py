"""Offline technical frame checks; pixel checks do not assess visual quality."""

import argparse
import json
import math
from pathlib import Path
import sys

try:
    from PIL import Image, ImageChops, ImageFilter, ImageStat
except ImportError:
    Image = None


CHECKS = ("input", "frames", "seam", "empty_frames", "rest_frame", "overflow", "fidelity")


def result(status, reason, **details):
    return {"status": status, "reason": reason, **details}


def number(value, name, positive=False, nonnegative=False):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value)):
        raise ValueError(f"{name} must be a finite number")
    if positive and value <= 0 or nonnegative and value < 0:
        raise ValueError(f"{name} is out of range")
    return value


def index(value, name, count):
    if type(value) is not int or not 0 <= value <= count:
        raise ValueError(f"{name} must be an integer in 0..{count}")
    return value


def resource_path(base, value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty path")
    if name == "frames_dir" and Path(value).is_absolute():
        raise ValueError("frames_dir must be relative to the manifest")
    return base / value


def read_image(path, mode="RGBA"):
    try:
        with Image.open(path) as source:
            return source.convert(mode)
    except (OSError, ValueError):
        raise ValueError(f"Cannot read image: {path.name}") from None


def equal(left, right, mask=None):
    # RGBA getbbox alone ignores differences confined to RGB on some Pillow versions.
    difference = ImageChops.difference(left, right)
    if mask is not None:
        difference = ImageChops.composite(difference, Image.new(left.mode, left.size), mask)
    return all(channel.getbbox() is None for channel in difference.split())


def verify(manifest):
    checks = {name: result("skipped", "Not configured or prerequisites unavailable")
              for name in CHECKS}
    report = {"ok": False, "checks": checks}
    if Image is None:
        checks["input"] = result("fail", "Pillow is required; use an interpreter with Pillow installed")
        return report
    try:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8-sig"),
                              parse_constant=lambda _: (_ for _ in ()).throw(ValueError("Nonstandard JSON number")))
        except OSError:
            raise ValueError(f"Cannot read manifest: {manifest.name}") from None
        except (ValueError, UnicodeError):
            raise ValueError(f"Invalid JSON: {manifest.name}") from None
        if not isinstance(data, dict):
            raise ValueError("Manifest must be an object")
        count = data.get("cycle_frames")
        if type(count) is not int or count < 1:
            raise ValueError("cycle_frames must be an integer >= 1")
        fps = number(data.get("fps"), "fps", positive=True)
        base = manifest.parent
        frames_dir = resource_path(base, data.get("frames_dir"), "frames_dir")
        lists = {}
        for key in ("empty_frames", "overflow_frames"):
            values = data.get(key, [])
            if not isinstance(values, list):
                raise ValueError(f"{key} must be an integer list")
            lists[key] = [index(value, key, count) for value in values]
        rest = index(data["rest_frame"], "rest_frame", count) if "rest_frame" in data else None
        images = {}
        for key in ("still", "mask"):
            if key in data:
                path = resource_path(base, data[key], key)
                images[key] = read_image(path, "L" if key == "mask" else "RGBA")
        if rest is not None and "still" not in images:
            raise ValueError("rest_frame requires still")
        if lists["overflow_frames"] and "mask" not in images:
            raise ValueError("overflow_frames requires mask")
        fidelity = data.get("fidelity")
        if "fidelity" in data:
            if not isinstance(fidelity, dict):
                raise ValueError("fidelity must be an object")
            if "still" not in images:
                raise ValueError("fidelity requires still")
            number(fidelity.get("min_psnr"), "fidelity.min_psnr")
            number(fidelity.get("blur"), "fidelity.blur", nonnegative=True)
            reference = resource_path(base, fidelity.get("reference"), "fidelity.reference")
            images["reference"] = read_image(reference, "RGB")
        checks["input"] = result("pass", "Manifest fields valid", cycle_frames=count, fps=fps)
    except (ValueError, OverflowError) as error:
        checks["input"] = result("fail", str(error))
        return report

    def frame(i):
        return read_image(frames_dir / f"{i:05d}.png")

    try:
        first = frame(0)
        for i in range(1, count + 1):
            if frame(i).size != first.size:
                raise ValueError(f"Frame size mismatch: {i:05d}.png")
        if "mask" in images and images["mask"].size != first.size:
            raise ValueError("mask size must match frames")
        if "still" in images and images["still"].size != first.size:
            raise ValueError("still size must match frames")
        if fidelity is not None and images["still"].size != images["reference"].size:
            raise ValueError("reference size must match still")
        checks["frames"] = result("pass", "All numbered frames exist and sizes match",
                                  count=count + 1, size=list(first.size))
    except ValueError as error:
        checks["frames"] = result("fail", str(error))
        return report

    def compare(name, pairs):
        failures = [i for i, target in pairs if not equal(frame(i), target)]
        checks[name] = result("fail" if failures else "pass", "Exact RGBA pixel comparison",
                              failed_frames=failures)

    try:
        compare("seam", [(count, first)])
        if lists["empty_frames"]:
            compare("empty_frames", [(i, first) for i in lists["empty_frames"]])
        if rest is not None:
            compare("rest_frame", [(rest, images["still"])])
        if "mask" in images:
            forbidden = images["mask"].point(lambda value: 255 if value == 0 else 0)
            if forbidden.getbbox() is None:
                checks["overflow"] = result("fail", "mask must contain at least one black pixel")
            elif lists["overflow_frames"]:
                failures = [i for i in lists["overflow_frames"] if not equal(frame(i), first, forbidden)]
                checks["overflow"] = result("fail" if failures else "pass",
                                            "Exact comparison on black mask pixels only",
                                            failed_frames=failures)
        if fidelity is not None:
            radius = fidelity["blur"]
            still = images["still"].convert("RGB").filter(ImageFilter.GaussianBlur(radius))
            reference = images["reference"].filter(ImageFilter.GaussianBlur(radius))
            stats = ImageStat.Stat(ImageChops.difference(still, reference))
            mse = sum(stats.sum2) / (still.width * still.height * 3)
            score = math.inf if mse == 0 else 10 * math.log10(255 ** 2 / mse)
            checks["fidelity"] = result("pass" if score >= fidelity["min_psnr"] else "fail",
                                        "RGB PSNR after Gaussian blur",
                                        score="inf" if math.isinf(score) else score,
                                        min_psnr=fidelity["min_psnr"], blur=radius)
    except (ValueError, OSError, OverflowError):
        checks["input"] = result("fail", "Cannot complete requested image comparison")
    report["ok"] = not any(item["status"] == "fail" for item in checks.values())
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    # Never overwrite a manifest or image, including through an output symlink.
    output = args.output
    if output is not None and (output.resolve() == args.manifest.resolve()
                               or output.suffix.lower() != ".json"):
        report = {"ok": False, "checks": {"input": result("fail", "Output must be a separate JSON file")}}
        output = None
    else:
        report = verify(args.manifest)
    serialized = json.dumps(report, ensure_ascii=True, allow_nan=False, indent=2) + "\n"
    if output is not None:
        try:
            # Exclusive creation protects existing inputs and reports from modification.
            with output.open("x", encoding="utf-8") as stream:
                stream.write(serialized)
        except OSError:
            report["ok"] = False
            report["checks"]["output"] = result("fail", f"Cannot create output: {output.name}")
            print(json.dumps(report, ensure_ascii=True, allow_nan=False, indent=2))
    else:
        print(serialized, end="")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
