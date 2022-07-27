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
import numpy as np
import sys, os

df = pd.read_excel('create-group.xlsx')
g_name = df['Group Name'].values.tolist()
g_part = df['Participants'].values.tolist()
dic={}

timeout_secs=200

browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists, timeout_secs=timeout_secs)


j=0
for grp in g_name:
    time.sleep(2)
    hbm = browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    hbm.click()
    time.sleep(1)
    cg = browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div[1]')
    cg.click()
    time.sleep(1)
    c_n = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div/div[1]/div/div/input')
    c_n.click()
    time.sleep(1)
    g_p = g_part[j].split(';')
    j = j + 1
    for i in g_p:
        try:
            k=0
            while k!=4:
                try:
                    k += 1
                    c_n.clear()
                    c_n.send_keys(i)
                    time.sleep(2)
                    user = browser.find_element_by_xpath(f'//span[@title="{i}"]')
                    user.click()
                    break
                except:
                    if k==4:
                        print('user {} not found in contacts!!!'.format(i))
                        dic[i] = 'no whatsapp contact found'
        except:
            print('user {} not found in contacts!!!'.format(i))
            dic[i] = 'no whatsapp contact found'
            cnt = len(i)
            for y in range(0,cnt):
                action = ActionChains(browser)
                action.send_keys_to_element(c_n, Keys.BACK_SPACE)
                action.perform()
    time.sleep(2)
    next_step = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div/span/div')
    next_step.click()
    time.sleep(2)
    grp_sub = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]')
    grp_sub.click()
    grp_sub.send_keys(grp)
    nxt = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div/span/div/div')
    nxt.click()
    time.sleep(5)
    try:
        time.sleep(2)
        invite = browser.find_element_by_xpath('/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div[2]/div/div')
        invite.click()
        time.sleep(2)
        send = browser.find_element_by_xpath('/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div/span/div')
        send.click()
        time.sleep(2)
        print('invite sent!!')
    except:
        print('all participants added to group!')

dfs = pd.DataFrame(data=dic, index=[0])
dfs = (dfs.T)
dfs.to_excel('no-whatsapp-no.xlsx')

kill_browser()
