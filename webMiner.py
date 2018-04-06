from selenium import webdriver

browser = webdriver.Chrome()
browser.get('url')
htmlHeaders = browser.find_elements_by_class_name("announceheader")
announceHeaders = [i.text for i in htmlHeaders]
print(announceHeaders)