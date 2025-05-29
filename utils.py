# utils.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("Error fetching HTML:", e)
        return ""

def parse_layoffs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'layoff-list-table'})

    if not table:
        print("Table not found.")
        return []

    rows = table.find('tbody').find_all('tr')
    layoffs = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 6:
            continue

        date_str = cols[0].get_text(strip=True)
        try:
            layoff_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ"
)
        except ValueError:
            continue

        layoffs.append({
            'Date': date_str,
            'Company': cols[1].get_text(strip=True),
            'Location': cols[2].get_text(strip=True),
            'Industry': cols[3].get_text(strip=True),
            '# Laid Off': cols[4].get_text(strip=True),
            '%': cols[5].get_text(strip=True)
        })

    return layoffs

def save_to_json(data, filename):
    # Remove datetime objects before saving
    for d in data:
        if 'layoff_date_obj' in d:
            d.pop('layoff_date_obj')
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Saved to {filename}")
    except Exception as e:
        print("Error saving JSON:", e)
