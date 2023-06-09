import requests
from bs4 import BeautifulSoup
 
def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
 
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
 
    # Find the relevant elements on the page and extract the desired information
    data = []
    # Example: Scraping headlines from a news website
    headlines = soup.find_all('h2', class_='headline')
    for headline in headlines:
        data.append(headline.text.strip())
 
    return data
 
# Example usage:
url = 'https://microsoftedge.microsoft.com/addons/detail/keyboard-mouse-for-xbox/ddgechhgijdmijagmnbhppbogpeflgih'  # Replace with the URL of the website you want to scrape
scraped_data = scrape_website(url)
 
# Print the collected data
for item in scraped_data:
    print(item)