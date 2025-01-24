import requests
from bs4 import BeautifulSoup

url = "https://plantops.uwaterloo.ca/service-interruptions/"  # Replace with the correct URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all <a> tags that contain the outage descriptions
    announcements = soup.find_all("a", class_="w3-leftbar")  # This assumes the outage descriptions are inside <a> tags with class="w3-leftbar"
    
    for announcement in announcements:
        # Print only the text within the <a> tag, which contains the description
        description = announcement.get_text(strip=True)  # strip=True removes extra whitespace
        if "CPH" in description and "electrical shutdown" in description.lower():
            print(description)
else:
    print("er")
