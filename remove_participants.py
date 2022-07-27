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

df = pd.read_excel('remove_participants.xlsx')
gn = df['Group Name'].values.tolist()
tpd = df['Participants to  remove']
tpd = tpd.tolist()

browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists,timeout_secs=timeout_secs )


k=0
list1 = []

timeout_secs=200
for i in gn:
    p_to_rem = tpd[k].split(';')
    k=k+1
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
    bl_info = browser.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/div/li[1]/div[1]')
    bl_info.click()
    time.sleep(1)
    # extend_list = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[3]/div[2]/div/div')
    # ex_list = extend_list.text
    # more = ex_list.split(' ')
    # if more[1] == 'more':
    #     extend_list.click()
    # else:
    #     print('very few participants for scrolling!!!')
    try:
        try:
            extend_list = browser.find_element_by_xpath(f'//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[2]/button')
        except:
            extend_list = browser.find_element_by_xpath(f'//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[5]/div[2]/button')
        ex_list = extend_list.text
        more = ex_list.split(' ')
        if more[1] == 'more' or more[1] == 'all':
            extend_list.click()
        else:
            print('very few participants for scrolling!!!')
    except:
        print('very few participant for scrolling.....')
    time.sleep(2)
    looptime = 2
    temp1 = 1
    while(looptime):
        scr1 = browser.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 400", scr1)
        element = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_3vPI2")))
        for j in range(0,len(element)):
            temp = element[j].text
            lst = temp.split('\n')
            lst1 = lst[0]
            for p in p_to_rem:
                if lst1 == p:
                    action = ActionChains(browser)
                    action.context_click(element[j]).perform()
                    time.sleep(2)
                    remove = browser.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/li[2]/div[1]')

                    rm = remove.text
                    if rm == 'Remove':
                        remove.click()
                        time.sleep(1)
                    else:
                        remove = browser.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/li[1]/div[1]')
                        remove.click()
                        time.sleep(1)
                    remove_1 = browser.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div')
                    remove_1.click()
                    time.sleep(3)
                    p_to_rem.remove(p)                                
        looptime = looptime - 1
                        
kill_browser()