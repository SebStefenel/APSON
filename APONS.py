import requests
from bs4 import BeautifulSoup

# URL of the PlantOps Service Interruptions page
url = "https://example.com/plantops-service-interruptions"

# Make a GET request to fetch the page content
response = requests.get(url)

# Check for successful response
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
    print(f"Failed to fetch the page. Status code: {response.status_code}")
