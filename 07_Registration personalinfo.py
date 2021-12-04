import time
from selenium import webdriver

from selenium.webdriver import ActionChains

#create instance for chrome browser
browser = webdriver.Chrome()


# browser.get to navigate to page
browser.maximize_window()
browser.get('https://www.cansrdev.com/clinical/dashboard/')

#verify title of the page
if(browser.title=="Cansr | Login"):
    print("Success: Cansr page logged")
else:
    print("Failed: Cansr page cannot be opened") 
time.sleep(2)
#find email path using xpath
email=browser.find_element_by_xpath("//input[@id='inp_loginid']")

#send text to element 
email.send_keys('clara80@yopmail.com')

#find password element using xpath
password=browser.find_element_by_xpath("//input[@id='inp_password']")

password.send_keys('Cansr@21')
time.sleep(3)

#select login button
login = browser.find_element_by_xpath("//button[text()='Login']")
login.click()
time.sleep(5)

#continue with registration
Registration = browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
time.sleep(5)
Registration.click()

#Personal Information
Info=browser.find_elements_by_xpath("//a[@id='steps-uid-0-t-0']")
#Info.click()
time.sleep(5)

#Personal info-title
title=browser.find_element_by_xpath("//select[@id='pr_title']")
title.send_keys('Ms.')
time.sleep(4)

#Gender
gender=browser.find_element_by_xpath("//select[@id='pr_gender']")
gender.send_keys('Female')
time.sleep(2)

#save & exit
save=browser.find_element_by_xpath("//button[contains(text(),'Save & Exit')]")
time.sleep(3)
save.click()

#confirmation
confirmation=browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]")
time.sleep(3)
confirmation.send_keys('Yes')

browser.close()







