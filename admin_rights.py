from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helium import *
# try:
#     from .utils import *
# except:
#     from utils import *
import time
# import autoit
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd


df = pd.read_excel('admin_only_send_message.xlsx')
gn = df['Group Name'].values.tolist()
rights = df['Rights'].values.tolist()

timeout_secs=200

browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists, timeout_secs=timeout_secs)

    

k = 0
for i in gn:
    search_box = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search_box.clear()
    search_box.send_keys(i)
    time.sleep(3)
    user = browser.find_element_by_xpath(f'//span[@title="{i}"]')
    user.click()
    time.sleep(2)
    hbm = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')
    hbm.click()  
    time.sleep(2)
    bl_info = browser.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/div/li[1]/div[1]')
    bl_info.click()
    time.sleep(1)
    settings = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[5]/div[4]/div/div')
    settings.click()
    send_message = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div/div/div')
    send_message.click()
    if rights[k] == 'Only admins':
        oa = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[2]/label')
        oa.click()
        confirm = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]')
        confirm.click()
        time.sleep(2)
    else:
        ap = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[1]/label')
        ap.click()
        confirm = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]')
        confirm.click()
        time.sleep(2)
    k = k + 1
    
kill_browser()