#######  install dependency ############
# pip3 install webdriver-manager
# pip3 install -U selenium
#######################################


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Listener
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

# # web driver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://play.typeracer.com?rt=2lobbruul0')
time.sleep(4)
# browser.find_element(By.XPATH, '//*[@id="gwt-uid-1"]/a').click()
#
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
            # time.sleep(0.07) # 120wpm
            # time.sleep(0.05) #188wpm
            time.sleep(0.02) #370wpm
    # by pressing 'delete' button to terminate the loop
    if key == Key.delete:
        return False

    # Collect all event until released
with Listener(on_press=show) as listener:
    listener.join()

