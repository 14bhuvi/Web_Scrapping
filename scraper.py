from datetime import datetime, timedelta
from request import get_response
import json
import os

# URL to fetch layoffs data (JSON)
url = "https://layoffs.fyi/data.json"

# Fetch JSON from the URL
response = get_response()
data = response

def save_to_json(data, filename):
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {path}")

def filter_last_7_days(data,column_id_map):
    recent = []
    today = datetime.utcnow().date()
    one_week_ago = today - timedelta(days=7)

    for item in data:
        cell_values = item.get("cellValuesByColumnId", {})
        news_item = {}
        for col_id in cell_values:
            col_name = column_id_map[col_id]
            news_item[col_name] = cell_values[col_id]
            

        try:
            layoff_date = datetime.strptime(news_item['Date Added'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
            if layoff_date >= one_week_ago:
                recent.append(news_item)
        except Exception as e:
                print(f"Error parsing date '{news_item['Date Added']}':", e)
    return recent

def main():
    print("=== Fetching JSON data ===")
    data = get_response()

    column_id_map={}
    for column in data["data"]["table"]["columns"]:
        column_id_map[column['id']] = column['name']
    
    # Extract rows safely
    rows = []
    try:
        rows = data["data"]["table"]["rows"]
    except (KeyError, TypeError):
        print("Error: Could not find rows in JSON data")

    print(f"Total entries fetched: {len(rows)}")

    filtered = filter_last_7_days(rows,column_id_map)
    print(f"Filtered {len(filtered)} entries from last 7 days.")
    save_to_json(filtered, "layoffs_last_week_from_json.json")

if __name__ == "__main__":
    main()
