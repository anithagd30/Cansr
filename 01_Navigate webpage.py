"""
SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Check the page title
4) Close the browser
"""
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

#quit browser window
#browser.quit



 

