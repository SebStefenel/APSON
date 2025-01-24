import requests
from bs4 import BeautifulSoup

url = "https://plantops.uwaterloo.ca/service-interruptions/"  # Replace with the correct URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("YAY")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
