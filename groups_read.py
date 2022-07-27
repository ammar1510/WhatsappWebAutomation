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

timeout_secs=200


df = pd.read_excel('group.xlsx')
li = df['Group Name'].values.tolist()


browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists,timeout_secs=timeout_secs )


for i in li:
    list1 = []
    search_box = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search_box.clear()
    search_box.send_keys(i)
    time.sleep(5)
    user = browser.find_element_by_xpath(f'//span[@title="{i}"]')
    user.click()
    time.sleep(2)
    hbm = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/div/span')
    hbm.click()  
    time.sleep(2)
    group_info = browser.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/div/li[1]/div[1]')
    group_info.click()
    time.sleep(5)
    try:
        try:
            extend_list = browser.find_element_by_xpath(f'//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[2]/button')
        except:
            extend_list = browser.find_element_by_xpath(f'//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[5]/div[2]/button')
        ex_list = extend_list.text
        more = ex_list.split(' ')
        if more[1] == 'more' or more[1] == 'all' :
            extend_list.click()
        else:
            print('very few participants for scrolling!!!')  
    except:
        print('very few participant for scrolling.....')
    time.sleep(2)
    looptime = 40
    temp1 = 1
    while(looptime):
        try:
            scr1 = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]')
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 400", scr1)
            element = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_2nY6U")))
            for j in range(0,len(element)):
                temp = element[j].text
                lst = temp.split('\n')
                lst1 = lst[0]
                for x in range(0, len(list1)):
                    if list1[x] == lst1:
                        temp1 = 0
                        break
                    else:
                        temp1 = 1
                if temp1 == 1:
                    list1.append(lst1)
        except:
            scr1 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[5]')
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 400", scr1)
            element = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_3OvU8")))
            for j in range(0,len(element)):
                temp = element[j].text
                lst = temp.split('\n')
                lst1 = lst[0]
                for x in range(0, len(list1)):
                    if list1[x] == lst1:
                        temp1 = 0
                        break
                    else:
                        temp1 = 1
                if temp1 == 1:
                    list1.append(lst1)
        looptime = looptime - 1   
    try:
        browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/header/div/div[1]/button/span').click()
    except:
        print("no clickable cross found...")
    dfs = pd.DataFrame(list1)
    dfs.to_excel('{}.xlsx'.format(i), index = False)




# for i in li:
#     list1 = []
#     search_box = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
#     search_box.clear()
#     search_box.send_keys(i)
#     time.sleep(5)
#     user = browser.find_element_by_xpath(f'//span[@title="{i}"]')
#     user.click()
#     time.sleep(2)
#     hbm = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
#     hbm.click()  
#     time.sleep(2)
#     bl_info = browser.find_element_by_xpath('//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[1]/div[1]')
#     bl_info.click()
#     time.sleep(5)
#     extend_list = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/button')
#     ex_list = extend_list.text
#     more = ex_list.split(' ')
#     if more[1] == 'more':
#         extend_list.click()
#     else:
#         print('very few participants for scrolling!!!')   
#     time.sleep(2)
#     looptime = 40
#     temp1 = 1
#     while(looptime):
#         scr1 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div')
#         browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 400", scr1)
#         element = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_3vPI2")))
#         for j in range(0,len(element)):
#             temp = element[j].text
#             lst = temp.split('\n')
#             lst1 = lst[0]
#             for x in range(0, len(list1)):
#                 if list1[x] == lst1:
#                     temp1 = 0
#                     break
#                 else:
#                     temp1 = 1
#             if temp1 == 1:
#                 list1.append(lst1)
#         looptime = looptime - 1   
#     dfs = pd.DataFrame(list1)
#     dfs.to_excel('{}.xlsx'.format(i), index = False)
    
kill_browser()
