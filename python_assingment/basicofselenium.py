from basicofselenium import webdriver
browser = webdriver.Chrome()  
browser.get("https://resilient-cendol-01c60b.netlify.app/")

print("Open Browser")
title = browser.title
print("Page Title:", title)

browser.quit()
