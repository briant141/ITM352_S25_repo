import urllib.request
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Open the URL
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
response = urllib.request.urlopen(url)

# Read and filter lines
for line in response:
    decoded_line = line.decode('utf-8')
    if "<title>" in decoded_line.lower():  # Case-insensitive check
        print(decoded_line.strip())
