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


df = pd.read_excel('add_participants.xlsx')
gn = df['Group Name'].values.tolist()
tpd = df['Participants to add']
tpd = tpd.tolist()

j=0
timeout_secs=200

df = pd.read_excel('add_participants.xlsx')
gn = df['Group Name'].values.tolist()
tpd = df['Participants to add']
tpd = tpd.tolist()

browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists,timeout_secs=timeout_secs )

for i in gn:
    p_to_add = tpd[j].split(';')
    # dfs = pd.read_excel('{}.xlsx'.format(i))
    # member = dfs[0].values.tolist()
    # for p in p_to_add:
    #     for m in member:
    #         if p == m:
    #             p_to_add.remove(p)
    j = j+1
    search_box = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search_box.clear()
    search_box.send_keys(i)
    time.sleep(5)
    user = browser.find_element_by_xpath(f'//span[@title="{i}"]')
    user.click()
    time.sleep(2)
    hbm = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
    hbm.click()  
    time.sleep(2)
    bl_info = browser.find_element_by_xpath('//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]/div[1]')
    bl_info.click()
    add_p = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[2]/div[1]/div[2]')
    add_p.click()
    for participants in p_to_add:
       for k in range(4):
           try:
               sm = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]')
               sm.clear()
               sm.send_keys(participants)
               time.sleep(2)
               name = browser.find_element_by_xpath(f'//span[@title="{participants}"]')
               time.sleep(1)
               name.click()
               break
           except:
               continue
        # try:
        #     # try:
        #     #     name = browser.find_element_by_xpath(
        #     #         '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/span/span')
        #     # except:
        #     #     name = browser.find_element_by_xpath(
        #     #         '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/span/span')
        #     # names = name.text
        #     # #             print(names)
        #     # #             print(participants)
        #     for k in range(10):
        #         name = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[k]/button/div[2]/div/div[2]')
        #         if name == participants:
        #             #print(name)
        #             name.click()
        #             time.sleep(2)
        # except:
        #     print('participant {} has no whatsapp contact!!!'.format(participants))
    select = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div')
    select.click()
    add = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div[2]')
    add.click()
    time.sleep(5)
    try:
        request = browser.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div[2]/div/div')
        request.click()
        send_req = browser.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div/span/div/span')
        send_req.click()
    except:
        print("participants added to group {} successfully!!!".format(i))

    print("participants added to group {} successfully!!!".format(i))
    
kill_browser()
