import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing mortgage rates
table = soup.find('table')

# Extract and print all rows in the table
rows = table.find_all('tr')

print(f"Total rows found (including header): {len(rows)}")


print("Bank Name | Rates")

# Skip the header (first row) and process the rest
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) > 1:
        bank = cols[0].get_text(strip=True)
        rates = ' | '.join(col.get_text(strip=True) for col in cols[1:])
        print(f"{bank} | {rates}")
