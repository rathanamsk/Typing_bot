from selenium import webdriver
from pynput.keyboard import Key, Listener
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

# # web driver
browser = webdriver.Chrome()
browser.get('https://play.typeracer.com?rt=4tpznkop1')# time.sleep(4)
# browser.find_element(By.XPATH,'//*[@id="gwt-uid-1"]/a').click()


def show(key):
    #press enter to start auto typing
    if key == Key.enter:
        browser.find_element(By.XPATH,'//*[@id="gwt-uid-22"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').click()
        words = browser.find_element(By.XPATH,('//*[@id="gwt-uid-22"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')).text
        # print(words)
        keyboard = Controller()
        def split_words(words):
            return [char for char in words]
        for i in split_words(words):
            keyboard.type(i)
            time.sleep(0.07)

    # by pressing 'delete' button
    # you can terminate the loop
    if key == Key.delete:
        return False


# Collect all event until released
with Listener(on_press=show) as listener:
    listener.join()

