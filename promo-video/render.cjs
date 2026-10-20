// Usage: node render.cjs <outDir> [fps] [t1,t2,... for stills]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [outDir, fpsArg = '30', stills] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'video.html'));
  await page.evaluate(() => document.fonts.ready);
  const fps = +fpsArg;
  const times = stills ? stills.split(',').map(Number) : Array.from({ length: 60 * fps }, (_, i) => i / fps);
  for (let i = 0; i < times.length; i++) {
    await page.evaluate(t => window.render(t), times[i]);
    const name = stills ? `still_${times[i]}.jpg` : `f${String(i).padStart(5, '0')}.jpg`;
    await page.screenshot({ path: path.join(outDir, name), type: 'jpeg', quality: 92 });
  }
  await browser.close();
})();
