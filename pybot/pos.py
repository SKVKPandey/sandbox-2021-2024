from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#identify element
l= driver.find_element_by_xpath("//img[@class='tp-logo']")
#get x, y coordinates
loc = l.location
#get height, width
s = l.size
print(loc)
print(s)
driver.close()