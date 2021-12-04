import time
from selenium import webdriver

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
time.sleep(5)

#select login button
login = browser.find_element_by_xpath("//button[text()='Login']")
login.click()
time.sleep(5)

#click here to continue
clickcontinue = browser.find_element_by_xpath("//u[contains(text(),'Click here to continue')]")
clickcontinue.click()
time.sleep(5)

#click purchase
purchase = browser.find_element_by_xpath("//a[@id='PKGCOS001']")
purchase.click()
time.sleep(3)

#consent form
consent = browser.find_element_by_xpath("//input[@id='consentCheckBox']")
consent.click()
time.sleep(3)

#continue to next page
submit = browser.find_element_by_xpath("//button[@id='agreeConsentId']")
submit.click()
time.sleep(2)

#Register
cardnumber=browser.find_element_by_xpath("//input[@id='cardNumber']")
cardnumber.send_keys(4242424242424242)
time.sleep(3)

#expiry month
month = browser.find_element_by_xpath("//select[@id='expiryMonth']")
month.send_keys('February')
time.sleep(0.8)

#expiry year
year = browser.find_element_by_xpath("//select[@id='expiryYear']")
year.send_keys(2022)
time.sleep(0.8)

#security code
code = browser.find_element_by_xpath("//input[@id='securityCode']")
code.send_keys(345)
time.sleep(0.8)

#address1
address1 = browser.find_element_by_xpath("//input[@id='cardHolderBilAddr1']")
address1.send_keys(122)

address2 = browser.find_element_by_xpath("//input[@id='cardHolderBilAddr2']")
address2.send_keys('Marcham Road')
time.sleep(0.8)

#country
country = browser.find_element_by_xpath("//select[@id='countryId']")
country.send_keys('United kingdom')
time.sleep(0.8)

#post code
postcode = browser.find_element_by_xpath("//input[@id='billingPostCode']")
postcode.send_keys('LL36 8LZ')
time.sleep(0.8)

#confirm
confirm = browser.find_element_by_xpath("//a[@id='confirmPaymentId']")
confirm.click()

#Agree&pay
agree = browser.find_element_by_xpath("//button[@id='payNowButtonId']")
agree.click()
time.sleep(0.8)

#continue with registration
#registration = browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
#registration.click()
#time.sleep(0.8)