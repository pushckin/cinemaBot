from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option('useAutomationExtension', False)

s = Service(executable_path='chromedriver_py')
driver = webdriver.Chrome(service=s)
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#   '''
# })

try:
    driver.maximize_window()
    driver.get('https://anycoindirect.eu')
    # driver.get('https://hdrezkasdf.org/')
    time.sleep(75)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()