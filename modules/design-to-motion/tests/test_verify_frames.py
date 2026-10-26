"""Independent CLI tests with generated fixtures; no network or installation."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image, ImageDraw


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_frames.py"


class VerifyFramesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="verify-frames-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "frames").mkdir()
        self.data = {"frames_dir": "frames", "cycle_frames": 2, "fps": 24}
        for i in range(3):
            self.save(f"frames/{i:05d}.png")

    def save(self, name, color=(20, 30, 40, 255), size=(12, 12)):
        Image.new("RGBA", size, color).save(self.root / name)

    def pixel(self, i, xy=(5, 5), color=(200, 30, 40, 255)):
        path = self.root / f"frames/{i:05d}.png"
        with Image.open(path) as source:
            image = source.convert("RGBA")
        image.putpixel(xy, color)
        image.save(path)

    def mask(self):
        mask = Image.new("L", (12, 12), 0)
        ImageDraw.Draw(mask).rounded_rectangle((1, 1, 10, 10), radius=4, fill=255)
        mask.save(self.root / "mask.png")
        self.data.update(mask="mask.png", overflow_frames=[1])

    def run_cli(self, output=False, python_args=()):
        manifest = self.root / "manifest.json"
        manifest.write_text(json.dumps(self.data), encoding="utf-8")
        args = [sys.executable, *python_args, str(SCRIPT), str(manifest)]
        if output:
            args += ["--output", str(self.root / "report.json")]
        process = subprocess.run(args, capture_output=True, text=True)
        raw = (self.root / "report.json").read_text(encoding="utf-8") if output else process.stdout
        report = json.loads(raw, parse_constant=lambda value: self.fail(f"Nonstandard JSON: {value}"))
        self.assertNotIn(str(self.root), raw)
        self.assertNotIn("C:\\\\Users", raw)
        self.assertEqual(process.stderr, "")
        self.assertEqual(process.returncode == 0, report["ok"])
        return report, process

    def test_correct_loop_with_all_checks_and_output(self):
        self.save("still.png")
        self.save("reference.png")
        self.mask()
        self.data.update(still="still.png", empty_frames=[1], rest_frame=1,
                         fidelity={"reference": "reference.png", "min_psnr": 40, "blur": 0.5})
        report, process = self.run_cli(output=True)
        self.assertTrue(report["ok"])
        self.assertEqual(process.stdout, "")
        self.assertTrue(all(item["status"] == "pass" for item in report["checks"].values()))
        self.assertEqual(report["checks"]["fidelity"]["score"], "inf")

    def test_wrong_seam_rgb_with_same_alpha(self):
        self.pixel(2)
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["seam"]["status"], "fail")

    def test_wrong_seam_alpha(self):
        self.pixel(2, color=(20, 30, 40, 0))
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["seam"]["status"], "fail")

    def test_missing_frame(self):
        (self.root / "frames/00001.png").unlink()
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["frames"]["status"], "fail")
        self.assertIn("00001.png", report["checks"]["frames"]["reason"])

    def test_size_mismatch(self):
        self.save("frames/00001.png", size=(8, 8))
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["frames"]["status"], "fail")

    def test_empty_state_ghost(self):
        self.pixel(1)
        self.data["empty_frames"] = [1]
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["empty_frames"]["failed_frames"], [1])
        self.assertFalse(report["ok"])

    def test_rest_does_not_return_to_still(self):
        self.save("still.png", color="white")
        self.data.update(still="still.png", rest_frame=1)
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["rest_frame"]["status"], "fail")

    def test_rounded_corner_overflow(self):
        self.mask()
        # (1, 1) is inside the card bounding box but outside its rounded corner.
        self.pixel(1, xy=(1, 1))
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["overflow"]["status"], "fail")

    def test_allowed_motion_and_unselected_entrance(self):
        self.mask()
        self.data["cycle_frames"] = 3
        self.save("frames/00003.png")
        self.pixel(1, xy=(5, 5))
        self.pixel(2, xy=(0, 0))  # Entrance is deliberately not selected.
        report, _ = self.run_cli()
        self.assertTrue(report["ok"])
        self.assertEqual(report["checks"]["overflow"]["status"], "pass")

    def test_mask_without_black_is_rejected_even_without_selected_frames(self):
        self.save("mask.png", color="white")
        self.data["mask"] = "mask.png"
        report, _ = self.run_cli()
        self.assertEqual(report["checks"]["overflow"]["status"], "fail")

    def test_mask_size_mismatch(self):
        self.save("mask.png", color="black", size=(8, 8))
        self.data["mask"] = "mask.png"
        report, _ = self.run_cli()
        self.assertFalse(report["ok"])

    def test_fidelity_failure_and_reported_threshold(self):
        self.save("still.png", color="black")
        self.save("reference.png", color="white")
        self.data.update(still="still.png",
                         fidelity={"reference": "reference.png", "min_psnr": 35, "blur": 0.5})
        report, _ = self.run_cli()
        fidelity = report["checks"]["fidelity"]
        self.assertEqual(fidelity["status"], "fail")
        self.assertEqual(fidelity["score"], 0.0)
        self.assertEqual(fidelity["min_psnr"], 35)

    def test_no_optional_checks_and_stdout_is_standard_json(self):
        report, _ = self.run_cli()
        self.assertTrue(report["ok"])
        for name in ("empty_frames", "rest_frame", "overflow", "fidelity"):
            self.assertEqual(report["checks"][name]["status"], "skipped")
        self.assertFalse((self.root / "report.json").exists())

    def test_empty_lists_do_not_count_as_pass(self):
        self.mask()
        self.data.update(empty_frames=[], overflow_frames=[])
        report, _ = self.run_cli()
        for name in ("empty_frames", "overflow"):
            self.assertEqual(report["checks"][name]["status"], "skipped")

    def test_invalid_manifest_fields(self):
        invalid = [
            {"cycle_frames": True}, {"cycle_frames": 0}, {"cycle_frames": 1.5},
            {"fps": 0}, {"fps": True}, {"fps": float("nan")},
            {"frames_dir": str(self.root)}, {"empty_frames": [True]},
            {"empty_frames": [3]}, {"empty_frames": "1"},
            {"rest_frame": 1}, {"overflow_frames": [1]}, {"still": "missing.png"},
            {"fidelity": None},
        ]
        for changes in invalid:
            with self.subTest(changes=changes):
                self.data = {"frames_dir": "frames", "cycle_frames": 2, "fps": 24, **changes}
                report, _ = self.run_cli()
                self.assertEqual(report["checks"]["input"]["status"], "fail")

    def test_invalid_fidelity_fields(self):
        self.save("still.png")
        self.save("reference.png")
        for changes in ({"blur": -1}, {"min_psnr": True}, {"reference": "missing.png"}):
            with self.subTest(changes=changes):
                self.data.update(still="still.png", fidelity={
                    "reference": "reference.png", "min_psnr": 30, "blur": 0.5, **changes})
                report, _ = self.run_cli()
                self.assertFalse(report["ok"])

    def test_missing_pillow_has_clear_nonzero_error(self):
        report, process = self.run_cli(python_args=("-S",))
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("Pillow is required", report["checks"]["input"]["reason"])

    def test_fidelity_size_contract(self):
        self.save("still.png", size=(8, 8))
        self.save("reference.png", size=(8, 8))
        self.data.update(still="still.png", fidelity={
            "reference": "reference.png", "min_psnr": 30, "blur": 0})
        report, _ = self.run_cli()
        self.assertFalse(report["ok"])
        self.assertEqual(report["checks"]["frames"]["status"], "fail")
        self.save("still.png")
        self.save("reference.png")
        report, _ = self.run_cli()
        self.assertTrue(report["ok"])
        self.save("reference.png", size=(9, 8))
        report, _ = self.run_cli()
        self.assertFalse(report["ok"])

    def test_missing_and_malformed_manifest(self):
        manifest = self.root / "bad.json"
        for content in (None, "{broken", "[]"):
            with self.subTest(content=content):
                if content is not None:
                    manifest.write_text(content, encoding="utf-8")
                process = subprocess.run([sys.executable, str(SCRIPT), str(manifest)],
                                         capture_output=True, text=True)
                self.assertNotEqual(process.returncode, 0)
                self.assertEqual(json.loads(process.stdout)["checks"]["input"]["status"], "fail")
                self.assertEqual(process.stderr, "")

    def test_output_cannot_overwrite_manifest(self):
        self.run_cli()
        manifest = self.root / "manifest.json"
        before = manifest.read_bytes()
        process = subprocess.run([sys.executable, str(SCRIPT), str(manifest), "--output", str(manifest)],
                                 capture_output=True, text=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertFalse(json.loads(process.stdout)["ok"])
        self.assertEqual(before, manifest.read_bytes())


if __name__ == "__main__":
    unittest.main()
