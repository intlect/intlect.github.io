import asyncio
from pyppeteer import launch

async def take_screenshot(url, screenshot_path):
    # Launch a headless browser
    browser = await launch()
    # Open a new page
    page = await browser.newPage()
    # Go to the URL
    await page.goto(url)
    # Wait for the content to load
    await page.waitForSelector('body')
    # Wait for 1 minute (60 seconds)
    await asyncio.sleep(60)
    # Take a screenshot
    await page.screenshot({'path': screenshot_path})
    # Close the browser
    await browser.close()

# Run the async function
url = 'http://127.0.0.1:5500/terminal.html?host=140.83.39.243:9999'
screenshot_path = 'screenshot.png'
asyncio.get_event_loop().run_until_complete(take_screenshot(url, screenshot_path))
print(f'Screenshot saved to {screenshot_path}')
