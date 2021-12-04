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

#find password element using xpath
password=browser.find_element_by_xpath("//input[@id='inp_password']")

password.send_keys('Cansr@21')
time.sleep(5)

#select login button
login = browser.find_element_by_xpath("//button[text()='Login']")
login.click()

#sleep to wait for loading above entries
time.sleep(4)

# Close the browser window
browser.close() 


        
