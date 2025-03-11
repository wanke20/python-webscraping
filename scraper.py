import requests, json, csv, os
from config import URL
from html_parser import extract_content

def scrape_website():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return None
    return response.text

def save_to_json(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Section", "Content"])
        for key, values in data.items():
            writer.writerow([key, " | ".join(values)])  # Join lists with "|"
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    html = scrape_website()
    if html:
        data = extract_content(html)
        save_to_json(data, "data/output.json")
        save_to_csv(data, "data/output.csv")
        print("Scraping complete! Data saved.")
