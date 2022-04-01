#for 每天傳送預約客戶簡訊 with 簡訊王


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import tkinter as tk
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def onOK():
    global a 
    a = (format(entry.get()))
    window.destroy()

window = tk.Tk()
window.title("phonenumber")
window.geometry("300x100+250+150")

alabel = tk.Label(window,text = "phone number")
alabel.pack()

entry = tk.Entry(window,
    width = 30)
entry.pack()

button =tk.Button(window,text = 'ok', command= onOK)
button.pack()

window.mainloop()

PATH = "D:/python/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

#登入
driver.get("https://www.kotsms.com.tw/index.php")
user = driver.find_element_by_id("usernames")
user.send_keys("KU")
user2 = driver.find_element_by_id("passwords")
user2.send_keys("Temp4321")
user2.send_keys(Keys.RETURN)

prompt = Alert(driver)
prompt.accept()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Image1"))
    )

#choose normal message
sendmessage = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[7]/td/div/a/img")
sendmessage.click()

#input number

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[2]/textarea"))
    )

phoneno = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[2]/textarea")
phoneno.send_keys(a)

#Submit /join
submit = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td/fieldset/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[3]/input")
submit.click()

#訊息內容
msgbox = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td/textarea")
msgbox.send_keys("GOGORO大安潮州服務中心您好，你的車輛已完工，因電話無人接聽，故傳簡訊通知，請於營業時間(早上0900-晚上2100)來取車，謝謝，祝您順心。電話:(02)23581077")

pas = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/table/tbody/tr[6]/td/input")
pas.click()

prompt.accept()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/fieldset/center/input[1]"))
    )
final = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/form/fieldset/center/input[1]")
final.click()
prompt.accept()
driver.quit()

