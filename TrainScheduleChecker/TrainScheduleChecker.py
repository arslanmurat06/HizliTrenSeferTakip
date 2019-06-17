
from selenium.webdriver import Firefox

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import date
import datetime

import time

number =0
print("Lütfen takip edilecek tarihi gün.ay.yıl formatında giriniz:")
takipEdilecekTarih = input()


def callWebsite():

    try:

        opts = Options()

        opts.set_headless()

        assert opts.headless

        browser =  Firefox (options =opts)
        browser.implicitly_wait(3)

        browser.get('https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf')


        nereden = browser.find_element_by_id('nereden')
        nereden.clear()
        nereden.send_keys('İstanbul(Halkalı)')


        print(browser.find_element_by_xpath("//input[contains(@id,'nereden')]").get_attribute('value'))


        nereye = browser.find_element_by_id('nereye')
        nereye.clear()
        nereye.send_keys('Ankara Gar')

        print(browser.find_element_by_xpath("//input[contains(@id,'nereye')]").get_attribute('value'))


        tarih = browser.find_element_by_id('trCalGid_input')
        tarih.clear()
        tarih.send_keys(takipEdilecekTarih)
        print(browser.find_element_by_xpath("//input[contains(@id,'trCalGid_input')]").get_attribute('value'))


        ara = browser.find_element_by_id('btnSeferSorgula')

        browser.execute_script("arguments[0].click()",ara)

        time.sleep(5)



        results = browser.find_element_by_id('mainTabView:gidisSeferTablosu:1:j_idt104:0:somVagonTipiGidis1_label')

        a = results.text.split(" ")[3]
        global number
        number = a[a.find("(")+1:a.find(")")]
    except:
        callWebsite()


    return int(number)




while number == 0:
    time.sleep(20)
    number = callWebsite()

    if number != 0:
        print("Boş koltuk var hemen rezervasyon yapın")

    else:
        print("Malesef boş koltuk yok")


#today = date.today()
#friday = today + datetime.timedelta( (4-today.weekday()) % 7 )

#print(friday.strftime("%d.%m.%Y"))

browser.close()





  
   


