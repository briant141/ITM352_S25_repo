import urllib.request
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Open the URL
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
with urllib.request.urlopen(url) as response:
    # html = response.read()
    
    # Decode from bytes to string
    # print(html.decode('utf-8')) 
    
    print(response)
