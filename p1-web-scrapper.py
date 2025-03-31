from playwright.sync_api import sync_playwright
import datetime

today = datetime.date.today()
formatted_today = today.strftime('%d-%m-%yy')
day_name = today.strftime("%A")
with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.accuweather.com/en/in/mussoori/1-196520_1_al/current-weather/1-196520_1_al', timeout=60000)
    temp = page.locator('div.display-temp').text_content()
    print(f'Temperature of Mussoorie on {day_name}, {formatted_today}: {temp}')
    browser.close()
