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

browser = start_chrome('https://web.whatsapp.com')
browser.fullscreen_window()
# wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
wait_until(Text('Now send and receive messages without keeping your phone online.').exists, timeout_secs=timeout_secs)


looptime = 100
list1 = []
temp1 = 1
while(looptime):
    try:
        scr1 = browser.find_element_by_xpath('//*[@id="pane-side"]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 400", scr1)
        element = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_3OvU8")))
        # print("element: {}".format(element))
        # print("length of element: {}".format(len(element)))
        for j in range(0, len(element)):
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
        time.sleep(1)
    except:
        break

# print(list1)
dfs = pd.DataFrame(list1)
dfs.to_excel('contacts.xlsx', index = False)

kill_browser()
