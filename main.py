# main.py
from request import get_response
from parser import parse_layoffs
import json

url = "https://layoffs.fyi/data.json"
html_content = get_response(url)
layoff_data = parse_layoffs(html_content)

# Save as JSON
with open('recent_layoffs.json', 'w') as f:
    json.dump(layoff_data, f, indent=2)

print("Saved", len(layoff_data), "recent layoff entries.")
