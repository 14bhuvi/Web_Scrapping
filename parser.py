# parser.py
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def parse_layoffs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'layoff-list-table'})

    if not table:
        print("Layoff table not found.")
        return []

    rows = table.find('tbody').find_all('tr')
    layoffs = []

    today = datetime.utcnow()
    last_week = today - datetime.timedelta(days=7)

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 6:
            continue  # Skip malformed rows

        date_str = cols[0].get_text(strip=True)
        try:
            # Convert string date to datetime object
            layoff_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            continue

        # Filter by last 7 days
        #fixed here
        if layoff_date >= last_week:
            layoff = {
                'Date': date_str,
                'Company': cols[1].get_text(strip=True),
                'Location': cols[2].get_text(strip=True),
                'Industry': cols[3].get_text(strip=True),
                '# Laid Off': cols[4].get_text(strip=True),
                '%': cols[5].get_text(strip=True),
            }
            layoffs.append(layoff)

    return layoffs
