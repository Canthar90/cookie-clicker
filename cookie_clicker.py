from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import datetime as dt
import keyboard
import time



def items_check():
    global previous
    previous = 0
    upgrades_we_can_buy = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    upgrades_to_be_count = [element.text for element in
                            driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")]
    print(f"lista do policzenia upadów dostępnych {upgrades_to_be_count} liczba {len(upgrades_to_be_count)}")
    print(f" Lista obiektów selenium : {upgrades_we_can_buy}")
    counter = 0
    for item in range(0, len(upgrades_we_can_buy)):
        action.click(on_element=upgrades_we_can_buy[-1-counter])
        action.perform()
        counter += 1





chrome_driver = "E:\chromedriver_ver97/chromedriver.exe"
s = Service(chrome_driver)
options = ChromeOptions()
driver = webdriver.Chrome(service=s, options=options)
action = ActionChains(driver=driver)
driver.get("https://orteil.dashnet.org/cookieclicker/")

giant_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

timeout = time.time() +5
fiwe_min = time.time() + 60*5
previous = 0
game_start = True
while game_start:
    now = dt.datetime.now()
    print(f"teraz {time.time()} przedtem {timeout}")
    if keyboard.is_pressed("esc") or time.time() > fiwe_min:
        cookies_per_sec = driver.find_element(By.CSS_SELECTOR, "#cookies div").text
        print(cookies_per_sec)
        game_start = False
    else:

        if time.time() > timeout:
            previous = dt.datetime.now()
            items_check()
            action.click(on_element=giant_cookie)
            action.perform()
        else:
            action.click(on_element=giant_cookie)
            action.perform()



