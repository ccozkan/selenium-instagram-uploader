import os
import time
from selenium import webdriver
from credentials import username, password, description_file


# FIREFOX
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
driver.set_window_size(360,640)


# CHROME/CHROMIUM

#from selenium.webdriver.chrome.options import Options
#mobile_emulation = {
#    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
#chrome_options = Options()
#chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#driver = webdriver.Chrome(chrome_options = chrome_options)


url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(url)
time.sleep(10)


field = driver.find_element_by_css_selector("input[type='text']")
field.send_keys(username)
field = driver.find_element_by_css_selector("input[type='password']")
field.send_keys(password)
time.sleep(2)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
button[0].click()


time.sleep(5)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
if len(button) > 0:
    button[0].click()

time.sleep(5)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Cancel')]")
if len(button) > 0:
    button[0].click()

time.sleep(2)
button = driver.find_elements_by_css_selector('[aria-label="New Post"]')
button[0].click()
#button1 = driver.find_elements_by_css_selector('[role="menuitem"]')
#button1[-1].click()

os.system('autokey-run -s select_image')

time.sleep(10)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Expand')]")
if len(button) > 0:
    button[0].click()

time.sleep(20)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Next')]")
button[0].click()

time.sleep(10)
field = driver.find_elements_by_tag_name('textarea')[0]
field.click()

with open(description_file, 'r') as file:
    description = file.read()

field.send_keys(description)

time.sleep(15)
button=driver.find_elements_by_xpath("//*[contains(text(), 'Share')]")
button[-1].click()


print('Success!')
time.sleep(15)
driver.quit()
