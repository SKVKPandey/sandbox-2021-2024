
from selenium import webdriver
from pyautogui import press, write, hotkey
from csv import reader
from time import sleep


with open('data.csv', 'r') as file:

  reader = reader(file)

  for row in reader:

    driver = webdriver.Chrome('chromedriver.exe') 
    driver.get(f'https://wa.me/91{row[0]}')

    press('left')
    press('enter')

    sleep(10)

    write("Hi")
    press("Enter")

    print(f'{row[0]} done!')

    sleep(2)

    hotkey('alt','f4')