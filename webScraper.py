from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.get('https://www.bseindia.com/corporates/List_Scrips.aspx?expandable=1')
browser.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddSegment']/option[text()='Equity']").click()
browser.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlStatus']/option[text()='Active']").click()
browser.find_element_by_name("ctl00$ContentPlaceHolder1$btnSubmit").click()
soup = BeautifulSoup(browser.page_source, "html.parser")
table = soup.find("table", attrs={"id": "ctl00_ContentPlaceHolder1_gvData"})
rows = table.findAll('tr')[2:-2]
headers = [x.getText() for x in rows[0].findChildren('th')]
rows = rows[1:]

data_table = []  # create an empty list to hold all the data
data_table = [[td.getText() for td in rows[i].findAll('td')]
               for i in range(len(rows))]

df = pd.DataFrame(data_table, columns=headers)
for i in range(10, 13):
    if i> 11:
        counter = (i%10)+2
    else:
        counter = i
    browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_gvData']/tbody/tr[1]/td/table/tbody/tr/td[" + str(counter) + "]/a").click()
    soup = BeautifulSoup(browser.page_source, "html.parser")
    table = soup.find("table", attrs={"id": "ctl00_ContentPlaceHolder1_gvData"})
    rows = table.findAll('tr')[3:-2]
    data_table = []  # create an empty list to hold all the data
    data_table = [[td.getText() for td in rows[i].findAll('td')]
                   for i in range(len(rows))]
    df_page = pd.DataFrame(data_table, columns=headers)
    df = df.append(df_page)
df.to_csv("tableToCsv.csv")