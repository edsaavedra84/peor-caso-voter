#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from proxy import proxy_chrome



usable_proxy = ["cl-san.pvdata.host",
                "ca-van.pvdata.host","ca-tor.pvdata.host","ca-mon.pvdata.host","bg-sof.pvdata.host",
                "br-sao.pvdata.host","be-bru.pvdata.host","at-wie.pvdata.host","au-syd.pvdata.host",
                "au-mel.pvdata.host","au-per.pvdata.host","au-bri.pvdata.host","ar-bue.pvdata.host",
                "br-sao.pvdata.host","us-sea.pvdata.host","us-pho.pvdata.host","us-nyc.pvdata.host",
                "us-jer.pvdata.host","us-mia.pvdata.host","us-los.pvdata.host","us-las.pvdata.host",
                "us-den.pvdata.host","us-dal.pvdata.host","us-chi.pvdata.host","us-buf.pvdata.host","us-atl.pvdata.host","ae-dub.pvdata.host","ua-nik.pvdata.host","uk-man.pvdata.host",
                "uk-lon.pvdata.host","tr-ist.pvdata.host","th-ban.pvdata.host","tw-tai.pvdata.host",
                "ch-zur.pvdata.host","se-sto.pvdata.host","se-kis.pvdata.host","se-got.pvdata.host",
                "es-mad.pvdata.host","kr-seo.pvdata.host","za-joh.pvdata.host","sk-bra.pvdata.host",
                "sg-sin.pvdata.host","rs-bel.pvdata.host","ro-buk.pvdata.host","pt-lis.pvdata.host",
                "pl-tor.pvdata.host","ph-man.pvdata.host","pe-lim.pvdata.host","pa-pan.pvdata.host",
                "no-osl.pvdata.host",
                "ng-lag.pvdata.host","nz-auc.pvdata.host","nl-ams.pvdata.host",
                "md-chi.pvdata.host","mx-mex.pvdata.host","mt-qor.pvdata.host","my-kua.pvdata.host",
                "lu-lux.pvdata.host","lt-sia.pvdata.host","lv-rig.pvdata.host","jp-tok.pvdata.host",
                "it-mil.pvdata.host","il-tel.pvdata.host","im-bal.pvdata.host","ie-dub.pvdata.host","ca-tor.pvdata.host","id-jak.pvdata.host",
                "in-mum.pvdata.host","in-ban.pvdata.host","is-rey.pvdata.host",
                "hu-bud.pvdata.host","hk-china.pvdata.host","hk-hon.pvdata.host","gr-ath.pvdata.host",
                "de-fra.pvdata.host","de-ber.pvdata.host","fr-par.pvdata.host","fi-esp.pvdata.host",
                "ee-tal.pvdata.host","dk-cop.pvdata.host","cz-pra.pvdata.host","cy-lim.pvdata.host",
                "hr-zag.pvdata.host","cr-san.pvdata.host","co-bog.pvdata.host",]



#votingfor = "40"
votingfor = "29"

for k in range (0, 60):
    print("Round number %s" % str(k) )
    for j in range (0, len(usable_proxy)):
        proxy = {
            'proxy': {
                'http': "http://VZQQbvPTUYHQZR3svZEb73bJ:eddie1@%s:8080" % usable_proxy[j],
                'https': "http://VZQQbvPTUYHQZR3svZEb73bJ:eddie1@%s:8080" % usable_proxy[j]
                }
            }
        print("setting driver opts")

        try:
            for m in range (0, 2):
                incognito = False
                if m == 1:
                    incognito = True

                # Using temp password for testing purposes!
                driver = proxy_chrome(usable_proxy[j], 8080, "VZQQbvPTUYHQZR3svZEb73bJ", "eddie1", incognito)
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
                    try:
                        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-id='"+votingfor+"']")))
                        element = driver.find_element(By.CSS_SELECTOR, "div[data-id='"+votingfor+"']").click()
                        time.sleep(1)     
                    except Exception as error:
                        print("An exception occurred", error)    
                        print("minor, just continue")
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
