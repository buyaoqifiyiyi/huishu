# 逐帧采集与导出

供[设计稿演示动画](../GUIDE.md)在明确需要视频/动图时使用。以下是与宿主接线的操作契约和示例，不是已安装的录制器；优先使用宿主允许且实际可用的浏览器自动化。工具缺失时报告缺项，不绕过宿主控制边界。

## 同一时间线驱动预览和采集

实时预览与导出使用同一套状态计算；将确定性时间与墙钟分开。可选页面约定：

- `?still`：无动画设计终态；等待字体和图片解码后截图。
- `?loop`：按照计划的完整周期播放与重置。
- `?capture`：关闭自身 rAF 推进，暴露 `__start()`、`__tick(dt)` 和 `__lt`，仅由采集器推进。不要同时让真实时钟再走一遍。

只为本次导出实现需要的模式，不要求把调试接口加进线上产品。一个时钟驱动计数、遮罩、路径、循环与辅助物。连续 CSS 关键帧与 JS 混用时必须纳入同一时间基准，否则截图虽齐全仍会漂移。

已经允许使用 Playwright 且该版本提供虚拟时钟时，可按如下思路适配：先安装虚拟时钟，再加载页面并等待资源，暂停后按帧推进。每帧毫秒数用相邻累计时间的差，避免 60fps 的 `1000/60` 截断累计漂移。

```javascript
// page、url、out、fps、N 由实际任务提供；不是可直接运行的独立CLI。
await page.clock.install({ time: 0 });
await page.goto(url, { waitUntil: 'load' }); // url 已包含页面约定的 capture 参数
await page.evaluate(async () => {
  await document.fonts.ready;
  await Promise.all([...document.images].map(im => im.decode()));
});
await page.clock.pauseAt(10000);
for (let i = 0; i <= N; i++) {
  if (i > 0) {
    const dt = Math.round(i * 1000 / fps) - Math.round((i - 1) * 1000 / fps);
    await page.clock.runFor(dt);
    await page.evaluate(dt => window.__tick(dt / 1000), dt);
  } else {
    await page.evaluate(() => window.__start());
  }
  // 若入场还使用CSS transitions，在这里按各自创建时刻seek；见下文。
  await page.screenshot({ path: `${out}/${String(i).padStart(5, '0')}.png` });
}
```

这个简例适用于所有动态值均由 `__tick` 显式绘制的页面；不能原样套到依赖真实 rAF 或未被控制的 CSS 动画上。页面的 `__start()` 必须先画周期0的约定首帧，`__tick()` 到一周期时执行完整重置，帧 N 用于接缝检查。

CSS transitions 如保留，记录每次状态变化的创建时间，采集时暂停其 Animation 并以对应标记设置 `currentTime`；新建的动画不能沿用旧循环标记。若无法准确统一时钟，改成按绝对时间计算属性的录制实现，并用同一实现预览；不要把不确定的录屏标为确定性逐帧采集。项目已有 Remotion 等机制时复用，不为采用本方法换栈。

## 检查范围

先采集静态设计终态和参考，再记录至少一个完整周期及验证端点。采样 manifest 见[模块说明](../GUIDE.md)。

- **接缝**：第0帧与第N帧一致；不把第N帧重复编码造成额外停顿。
- **空态**：检查重置后的整个空态区间；只测周期边界抓不到中间残影。
- **恢复**：最后一个故事结束、淡出前应回到设计终态。需要停顿时明确恢复帧范围。
- **越界**：应用框架外或卡片真实轮廓外的区域保持背景一致；入场阶段用对应轮廓，故事阶段用固定轮廓。掩码包含真实阴影和必要抗锯齿容差。
- **视觉**：查看多个中间帧拼图，并实际播放导出文件，确认功能叙事、清晰度、节奏和循环。确定性差分不能代替观看。

有意运动的背景/阴影或被允许的镜头变化应进入计划与检查区域，不用全白掩码绕过越界检查。不借模糊PSNR宣称逐像素一致；如确需像素相同，使用未模糊的精确差分并报告失败区域。

## 按实际要求编码

核对已安装 FFmpeg 与实际分发目标要求；以下是通用示例参数，不承诺任何平台当前上传限制。`N` 是用于编码的帧数，不含验证端点。帧率须与采集一致，尺寸与GIF帧率按目标决定。

```text
ffmpeg -framerate 30 -start_number 0 -i frames/%05d.png -frames:v 120 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart demo.mp4
```

H.264 4:2:0 使用偶数尺寸；需要裁切一像素时明确报告，也可在保持构图前提下补边。GIF 按内容裁切或等比缩放，不能为了填满固定比例拉伸设计。照片背景补边需遵循源画面与用户要求。

```text
ffmpeg -framerate 30 -start_number 0 -i frames/%05d.png -filter_complex "trim=end_frame=120,fps=15,scale=800:-2:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" -loop 0 demo.gif
```

GIF 过大时按清晰度与叙事需要调整帧率、色数和尺寸，不把示例文件大小当保证。编码后用可用媒体探测工具读取实际尺寸、时长、帧率与帧数，并在播放器实际打开。明确区分“文件成功编码”和“实际观看已验收”。

采集页、帧序列和临时浏览器保持任务隔离；结束后关闭本任务创建的浏览器实例与服务，保留所需交付，不关闭用户原有会话。Figma令牌、宿主配置、源业务素材不进入技能包或公开示例。

来源：选择性改编自 Elaya `ai-design-skills@a2735a3` 的设计稿动画方法；[MIT许可](../../../licenses/Elaya-ai-design-skills-MIT.txt)。虚拟时钟示例与参数由本地兼容改写，接口依据 [Playwright Clock](https://playwright.dev/docs/clock) 与 [FFmpeg官方文档](https://ffmpeg.org/ffmpeg.html)核对；具体宿主/API可用性仍须在执行任务时核实。

## 2026-10-27：落定帧与独立静态参考

若同一元素经过过渡后与单独 `?still` 截图仅有栅格化差异，先保存入场结束、首个故事开始前的落定帧。淡出前的恢复帧应与这张同时间线落定帧精确一致；再把落定帧与独立静态设计参考比较，查看结构差异并报告实际PSNR/模糊参数，不套用通用阈值代替看图。

现有检查器无需换版：manifest 可用 `"still": "landed.png"`、`"fidelity": {"reference": "static-reference.png", "min_psnr": 40, "blur": 0}`。数值仅说明字段，实际判据预先按本任务固定；源图、采集尺寸及参考身份各自保存。`rest_frame` 检查精确恢复到landed，fidelity只说明landed与独立参考的差异。不能把landed复制成独立参考后声称还原已验。接缝和空态仍对照第0帧，沿用原有语义。

选择性依据：[Elaya固定源](https://github.com/elayadesign/ai-design-skills/blob/5e578402da175cdc539c900e4b09ceecfadcb37c/skills/design-to-motion/SKILL.md)。未采用强制首屏入场、固定时长/尺寸与导出三件套。
