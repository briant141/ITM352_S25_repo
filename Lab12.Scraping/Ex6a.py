import requests
from bs4 import BeautifulSoup

# Fetch the page
url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find the rate table
table = soup.find('table')

# Extract each row
rows = table.find_all('tr')

# Print number of rows extracted (including header)
print(f"Number of rows found: {len(rows)}")

