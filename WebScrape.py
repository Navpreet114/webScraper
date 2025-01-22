from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.chrome.service
import csv

driver = webdriver.Chrome()

page_url = 'https://steamdb.info/charts/'

#fetch the webpage
driver.get(page_url)

#Wait for the table to load (adjustable)
driver.implicitly_wait(10)

#Get the page source after JS execution
page_source = driver.page_source

#Parse the html content
soup = BeautifulSoup(page_source, 'html.parser')

#Find the table element
table = soup.find('table', class_='table-products table-hover text-left dataTable')


if table:
    #Extract column headers
    headers = [th.get_text().strip() for th in table.find_all('th')]
    
    #Extract the row data
    rows = []
    for tr in table.find_all('tr'):
        row = [td.get_text().strip() for td in tr.find_all('td')]
        if row:
            rows.append(row)
            
    print('Column headers:')    
    print(headers)  
    
    print('\nRow data:')
    for row in rows:
        print(row)    
    
    print("Data saved to file successfully!") 
else:
    print("Table not found")
    
#close the web driver from selenium
driver.quit()
