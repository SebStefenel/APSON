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
    
    # Extract relevant information (modify based on your inspection)
    announcements = soup.find_all("div", class_="announcement-class")  # Replace with actual HTML tags and classes
    
    for announcement in announcements:
        # Extract date, time, duration, and description
        date = announcement.find("span", class_="date-class").text  # Replace with actual tags
        time = announcement.find("span", class_="time-class").text  # Replace with actual tags
        duration = announcement.find("span", class_="duration-class").text  # Replace with actual tags
        description = announcement.text  # Or refine with other tags
        
        # Print the extracted details
        print(f"Date: {date}, Time: {time}, Duration: {duration}")
        print(f"Description: {description}")
else:
    print(f"Fetch the page")
