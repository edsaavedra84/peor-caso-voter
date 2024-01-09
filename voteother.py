#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver

# import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from proxy import proxy_chrome

from seleniumwire import webdriver


usable_proxy = ["syd.socks.ipvanish.com",
"tor.socks.ipvanish.com",
"par.socks.ipvanish.com",
"fra.socks.ipvanish.com",
"lin.socks.ipvanish.com",
"nrt.socks.ipvanish.com",
"ams.socks.ipvanish.com",
"waw.socks.ipvanish.com",
"lis.socks.ipvanish.com",
"sin.socks.ipvanish.com",
"sto.socks.ipvanish.com",
"lon.socks.ipvanish.com",
"iad.socks.ipvanish.com",
"atl.socks.ipvanish.com",
"chi.socks.ipvanish.com",
"dal.socks.ipvanish.com",
"den.socks.ipvanish.com",
"lax.socks.ipvanish.com",
"mia.socks.ipvanish.com",
"nyc.socks.ipvanish.com",
"phx.socks.ipvanish.com",
"sea.socks.ipvanish.com"]

#votingfor = "40" UHh7jf73mr aojxUyYEPT
votingfor = "29"

for k in range (0, 60):
    print("Round number %s" % str(k) )
    for j in range (0, len(usable_proxy)):
        options = {
            'proxy': {
                'http': "socks5://UHh7jf73mr:aojxUyYEPT@%s:1080" % usable_proxy[j],
                'https': "socks5://UHh7jf73mr:aojxUyYEPT@%s:1080" % usable_proxy[j]
                }
            }
        print("setting driver opts")

        try:
            #driver = proxy_chrome(usable_proxy[j], 1080, "UHh7jf73mr", "aojxUyYEPT")
            driver = webdriver.Chrome(seleniumwire_options=options)
            time.sleep(2)
            driver.set_page_load_timeout(30)
            print("opening url")
            driver.get("https://www.xencelabs.com/xencelabs-drawing-challenge-peace-on-earth-work-display?lang_select=en")

            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='f_po f_18']")))
            driver.execute_script("window.scrollTo(0, 500)")
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='f_po f_18']")))
            driver.find_element(By.XPATH, "//p[@class='f_po f_18']").click()
            
            counter = 1
            VisibleError = True
            while VisibleError and counter < 5:
                try:
                    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-id='"+votingfor+"']")))
                    time.sleep(2)
                    VisibleError = False
                except Exception as error:
                    print("not visible, scrolling")
                    counter = counter + 1
                    driver.execute_script("window.scroll(0,700+window.scrollY)")


            #driver.execute_script("window.scrollTo(0, 1000)")
            #time.sleep(2)
            #driver.execute_script("window.scrollTo(0, 2000)")
            #time.sleep(2)
            loc = driver.find_element(By.CSS_SELECTOR, "div[data-id='"+votingfor+"']").location
            driver.execute_script("window.scrollTo(0,"+str(loc["y"]-200)+")")
            
            print("proxy -> " + str(usable_proxy[j]))

            #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "li_"+votingfor)))
            elementNum = str(driver.find_element(By.ID, "li_"+votingfor).text).split()[2]
            print("current -> " + str(elementNum))

            if k == 0 or k == 29:
                with open("shopping_memo.txt", "a") as f:
                    f.write("current -> " + str(elementNum))  

            # vote 6 times...
            for i in range(0, 6):
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-id='"+votingfor+"']")))
                element = driver.find_element(By.CSS_SELECTOR, "div[data-id='"+votingfor+"']").click()
                time.sleep(1)            
        except Exception as error:
            print("An exception occurred", error)    
            print("closing")
            driver.close()
            time.sleep(2)       
            continue
        
        print("closing")
        driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)
        print("--------------")