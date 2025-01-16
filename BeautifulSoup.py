from bs4 import BeautifulSoup
import requests

#fetch the webpage content
url = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401"
response = requests.get(url)
html_content = response.content

#Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

#extract specific element
table = soup.find(id="simpleTable")

print(table)

if table:
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        for cell in cells:
                print(cell.text.strip())

else:
    print("No table is found")
