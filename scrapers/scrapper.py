import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import json

# Base URL for the main monster list and pattern for JSON files
MAIN_URL = "https://www.completecompendium.com/appendix/"
BASE_URL_PATTERN = "https://www.completecompendium.com/page-data/appendix/{}/page-data.json"

# Function to get all monster names from the main page
def get_monster_names():
    response = requests.get(MAIN_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    monster_names = []

    # Extract all monster names and URLs
    for link in soup.select("a[href^='/appendix/']"):  # Adjust selector if necessary
        name = link['href'].split('/')[-2]  # Extract name from the URL
        monster_names.append(name)
    
    return monster_names

# Function to recursively search for monster data in nested JSON structures
def find_monster_data(data, monster_name):
    if isinstance(data, dict):
        if data.get("monster_key") == monster_name:
            return data.get("monster_data", {})
        for key, value in data.items():
            result = find_monster_data(value, monster_name)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_monster_data(item, monster_name)
            if result:
                return result
    return None

# Function to scrape monster details from JSON
def scrape_monster_detail_from_json(monster_name):
    url = BASE_URL_PATTERN.format(monster_name)
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        monster_data_section = find_monster_data(json_data, monster_name)
        
        if monster_data_section:
            statblock = monster_data_section.get("statblock")
            if statblock:
                monster_key = list(statblock.keys())[0]
                stats = statblock[monster_key]
                monster_data = {"Name": monster_key}
                for key, value in stats.items():
                    monster_data[key] = value
                return monster_data

            full_body_html = monster_data_section.get("fullBody", "")
            if full_body_html:
                soup = BeautifulSoup(full_body_html, 'html.parser')
                monster_data = {"Name": monster_name.capitalize()}
                for row in soup.find_all("tr"):
                    label = row.find("th")
                    value = row.find("td")
                    if label and value:  # Check if both label and value are found
                        monster_data[label.get_text(strip=True).replace(":", "")] = value.get_text(strip=True)
                return monster_data
        
        return None
    else:
        return None

# Main function to scrape data for all monsters
def scrape_all_monsters():
    monster_names = get_monster_names()
    total_monsters = len(monster_names)
    print(f"Found {total_monsters} monsters to scrape.")

    all_monsters = []
    for index, name in enumerate(monster_names):
        print(f"Processing: {name} ({index + 1}/{total_monsters})")
        monster_data = scrape_monster_detail_from_json(name)
        if monster_data:
            all_monsters.append(monster_data)
        
        # Display progress percentage
        progress_percentage = ((index + 1) / total_monsters) * 100
        print(f"Progress: {progress_percentage:.2f}%")

        time.sleep(1)  # Avoid overloading the server

    # Convert to DataFrame and save
    df = pd.DataFrame(all_monsters)
    df.to_csv("monsters_data.json_scraped.csv", index=False)
    print("Data saved to monsters_data.json_scraped.csv")

# Run the scraper
scrape_all_monsters()
