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

#click on signup
signup=browser.find_element_by_xpath("//a[contains(text(),'Sign Up')]")
signup.click()
time.sleep(20)

#create Fname
fname=browser.find_element_by_xpath("//input[@id='inp_firstName']")
#send value to element
fname.send_keys('clara')
time.sleep(10)

#create Lname
lname=browser.find_element_by_xpath("//input[@id='inp_LastName']")
#send value to lname element
lname.send_keys('larson')
time.sleep(20)

#Email 
email=browser.find_element_by_xpath("//input[@id='email']")
#send value to email
email.send_keys('clara80@yopmail.com')
time.sleep(20)

#Postcode
postcode=browser.find_element_by_xpath("//input[@id='postcode']")
#value to postcode element
postcode.send_keys('CH7 6TU')


#date of birth entries
#date
date=browser.find_element_by_xpath("//select[@id='dobDate']")
date.send_keys('18')

#month
month=browser.find_element_by_xpath("//select[@id='dobMonth']")
month.send_keys('July')

#year
year=browser.find_element_by_xpath("//select[@id='dobYear']")
year.send_keys('1980')



#Captcha
captcha=browser.find_element_by_xpath("//input[@id='txtInput']")
time.sleep(10)


#signup consent
#checkbox=browser.find_element_by_xpath("//input[@name='signup-consent']")
checkbox=browser.find_element_by_xpath("//input[@id='signup-consent']")
checkbox.click()
time.sleep(10)


#submit
submit=browser.find_element_by_xpath("//button[@id='SignupBut_signup']")
submit.click()

