from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.chrome.service

driver = webdriver.Chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#fetch the webpage
driver.get(page_url)

#wait for the table to load (adjustable)
driver.implicitly_wait(10)

#Get the page source after JS execution
page_source = driver.page_source

#parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

#find the table element
table = soup.find('table', class_='pub-table')

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
