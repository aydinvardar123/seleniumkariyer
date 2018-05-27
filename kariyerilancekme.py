
import os
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time
import select

class den():
    def giris(self):
        driver = webdriver.Chrome()
        idi = driver.find_element_by_id
        name = driver.find_element_by_name
        xpat = driver.find_element_by_xpath
        calas = driver.find_element_by_class_name
        isim = driver.find_elements_by_partial_link_text
        cisim = driver.find_element_by_link_text

        driver.get("http://www.kariyer.net/website/kariyerim/login.aspx")
        idi("lgnUserName").clear()
        idi("lgnUserName").send_keys("kullanıcı isimi gir")
        idi("lgnPassword").clear()
        idi("lgnPassword").send_keys("şifre gir")
        calas("btn").click()

        driver.get("http://www.kariyer.net/is-ilanlari")
        idi("txtSearchKeyword").clear()
        idi("txtSearchKeyword").send_keys("ronesans")
        idi("btnSearchKeyword").click()
        self.giris = driver.page_source
        self.driver=driver
        soup= BS(self.driver.page_source,'html.parser')
        for a in soup.findAll("a", { "id" : "lnkLastPage" }):
            self.a =int(a.text[0])
            print int(a.text[0]),"sayfa ilan mevcut"
            time.sleep(1)
        for bul in soup.findAll("span", { "id" : "totalJobCount" }):
            sayac = bul.text
        print sayac," adet ilan var"
                
    
    def ilan(self):
        try:
            liste = []
            soup= BS(self.driver.page_source,'html.parser')
            for d in range(self.a):
                for i in soup.findAll("a", { "class" : "link position" }):
                    for c in soup.findAll("a", { "class" : "link company" }):
                        self.c = c.text
                        has = c.text
                    #for b in i.findAll("a"):
                    g= i.get("href")
                    bas = i.text
                    print "-"*20
                    print bas
                    print "-"*20
                    #time.sleep(0.5)
                    print has
                    print "www.kariyer.net"+g
                   
                
            xpat = self.driver.find_element_by_xpath
            xpat("//*[@id='lnkNextPage']").click()
            time.sleep(5)
            soup= BS(self.driver.page_source,'html.parser')
            print "*"*20,int(d+1),". SAYFA SONU","*"*20
        except:
            print "*"*20,int(d+1),". SAYFA SONU","*"*20

    def bak(self):
        print self.fiske
        
        
    def kapa(self):
        print "*"*50
        print self.c
        print "*"*50
        self.driver.close()


    
        
a = den()
a.giris()
a.ilan()

a.kapa()
    
