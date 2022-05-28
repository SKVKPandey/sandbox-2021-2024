from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyautogui import press
import time

driver = webdriver.Chrome('C:/Drivers/WebDriver/chromedriver.exe') #Drive_Address
driver.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653476060&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded19b33f-25c3-b2f9-7ec9-4a74b91fdab7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='loginfmt']")


username.send_keys('''someone@example.com''') 

time.sleep(0.5)

submit = driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)

password = driver.find_element_by_xpath("//input[@name='passwd']")

password.send_keys('''git@root123''')
time.sleep(0.5)

submit = driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)

submit = driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)

driver.get('https://outlook.live.com/mail/0/')
time.sleep(10)

while True:

    try:

        submit = driver.find_element_by_xpath("//div[@role='option']").click()
        time.sleep(10)

        submit = driver.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span/i[2]').click()
        time.sleep(4)
      
        press('down')
        press('enter')
        time.sleep(2)

    except Exception as e:
        print(e)
        break


 # submit = driver.find_element_by_xpath('//*[@id="ok-7"]/span/span').click()
        # actions = ActionChains(driver)
        # actions.move_by_offset(0,630).click().perform()
        # l= driver.find_element_by_xpath('//*[@id="ok-7"]/span/span')
        # #get x, y coordinates
        # loc = l.location
        # #get height, width
        # s = l.size
        # print(loc)
        # print(s)