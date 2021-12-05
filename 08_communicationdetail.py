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
time.sleep(3)

#address line1
line1=browser.find_element_by_xpath("//input[@id='pr_firstline']")
line1.send_keys('93 Caradon Hill')
time.sleep(3)

#town/city
town=browser.find_element_by_xpath("//input[@id='pr_countrydist']")
town.send_keys('BRINKLOW')
time.sleep(3)

#zipcode
zipcode=browser.find_element_by_xpath("//input[@id='pr_postcode']")
zipcode.send_keys('CH7 6TU')

#country
country=browser.find_element_by_xpath("//select[@id='pr_country']")
country.send_keys('United Kingdom')
time.sleep(3)

#countrycode
country=browser.find_element_by_xpath("//select[@id='country_code']")
country.send_keys('+44- United Kingdom')
time.sleep(3)

#contact number
contact=browser.find_element_by_xpath("//input[@id='pr_mobile']")
contact.send_keys('078 8108 1075')
time.sleep(3)

#next button
next=browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)



