import requests
from bs4 import BeautifulSoup
from icecream import ic
import json


# Enable cookies and JavaScript in requests, parse webpage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}
session = requests.Session()
webpage_response = session.get("https://www.beeradvocate.com/beer/styles/", headers=headers)
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# Find all "<a>" elements
style_links = soup.find_all("a")
styles = {}

# Filter for beer styles and ending number(s) in "href"
for link in style_links:
    linky = link.get("href")
    if linky and "beer/styles/" in linky and linky[-2].isnumeric():
        styles.append(link.get_text())

# Print confirmation
# ic(styles)

# Write to styles.json
with open("style.json", "w") as f:
    json.dump(styles, f)