import pandas as pd
import requests
from bs4 import BeautifulSoup

# Scrape data from web page
url = 'https://www.mergermarket.com/homepage'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]

# Export to Excel file
df.to_excel('scraped_data.xlsx', index=False)
