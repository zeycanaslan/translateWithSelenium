import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


kelime=input("bir kelime gir: ")

driver=webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

#bir öğenin varlığını veya görünürlüğünü kontrol etmek için kullanılır.
presence = EC.presence_of_element_located  # "varlık kontrolü"
visible = EC.visibility_of_element_located  # "görünürlük kontrolü"

driver.get("https://translate.google.com/")

dil = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[1]/c-wiz/div[1]/c-wiz/div[2]/button/div[3]")))
dil.click()

sec = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/div[124]/div[2]")))
sec.click()


time.sleep(5)
dil2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]")))
dil2.click()

time.sleep(5)

sec2=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[71]/div[2]")))
sec2.click()


gir=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")))
gir.send_keys(kelime)
time.sleep(3)

ceviri=wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]")))
print("Çeviri: {}" .format(ceviri.text))


driver.quit()



"""BU ÇEVİRİ KISA VE DİREKT ÇEVİRİ KÜTÜPHANESİ İLE YAPILDI
from googletrans import Translator

translator = Translator()
dt1 = translator.translate(text='nasılsın', src='tr', dest='ku')
print(dt1.text)
"""
