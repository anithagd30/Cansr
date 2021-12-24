import time
from selenium import webdriver

#create instance for chrome browser
browser = webdriver.Chrome()


# browser.get to navigate to page
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
email.send_keys('morgan78@yopmail.com')

forgotpassword=browser.find_element_by_xpath("//a[contains(text(),'Forgot Password / Email')]")
forgotpassword.click()

email=browser.find_element_by_xpath("//input[@id='inp_emailid']")
email.send_keys('morgan78@yopmail.com')

button_click=browser.find_element_by_xpath("//button[contains(text(),'Continue')]").click()  


