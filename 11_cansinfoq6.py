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

#my account
account=browser.find_element_by_xpath("//a[@id='newmyProfileLink-old']")
time.sleep(3)
account.click()

#click registration
Registraion=browser.find_element_by_xpath("//a[@id='newmyProfileLinkRenamed']")
Registraion.click()
time.sleep(3)

#click next
next=browser.find_element_by_xpath("//a[@href='#next']")
next.click()
time.sleep(4)

#previous diagnosis
q6=browser.find_element_by_xpath("//input[@id='no_cancer']")
time.sleep(3)
q6.click()


#q7
q7=browser.find_element_by_xpath("//input[@id='no_cancer_relative']")
q7.click()
time.sleep(3)

#q8
q8=browser.find_element_by_xpath("//input[@id='no_cancer_other']")
q8.click()
time.sleep(3)

#next
next=browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)