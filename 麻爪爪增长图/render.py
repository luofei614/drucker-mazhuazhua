from playwright.sync_api import sync_playwright
import pathlib

html_path = pathlib.Path("/Users/luofei/Desktop/麻爪爪游学/麻爪爪增长图/麻爪爪增长图.html").resolve()
out_path = html_path.with_suffix(".png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page.goto(html_path.as_uri())
    page.wait_for_timeout(400)
    page.screenshot(path=str(out_path), clip={"x": 0, "y": 0, "width": 1920, "height": 1080})
    browser.close()

print("PNG saved:", out_path, out_path.stat().st_size, "bytes")
