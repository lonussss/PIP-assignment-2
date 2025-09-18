

import json                                     #importing required packages
import os                               
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://events.nyu.edu"                  #nyu events page    

def scrape_events():
    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(URL)

    # Wait until events are present
    wait = WebDriverWait(driver, 15)
    event_blocks = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.lw_cal_event"))
    )

    events = []
    for e in event_blocks:
        # Title + URL
        title_el = e.find_element(By.CSS_SELECTOR, ".lw_events_title a")
        title = title_el.text.strip()
        url = title_el.get_attribute("href")

        # Date/Time
        date_el = e.find_element(By.CSS_SELECTOR, ".nyu-date-time")
        date_time = date_el.text.strip() if date_el else "N/A"

        # Location (inside <p>)
        loc_el = e.find_elements(By.TAG_NAME, "p")
        location = loc_el[0].text.strip() if loc_el else "N/A"

        events.append({
            "title": title,
            "date_time": date_time,
            "location": location,
            "url": url
        })

    driver.quit()
    return events

def scrape_with_retries(max_retries=3):
    """Retry scraping a few times before failing."""
    for attempt in range(1, max_retries + 1):
        try:
            return scrape_events()
        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                raise

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from validators import validate_events

if __name__ == "__main__":
    data = scrape_events()

    errors = validate_events(data)
    if errors:
        print("⚠️ Validation issues found:")
        for idx, errs in errors.items():
            print(f"  Event {idx}: {errs}")
    else:
        print("✅ All events passed validation.")

    # Save only if valid
    from pathlib import Path
    project_root = Path.cwd()
    data_folder = project_root / "data"
    data_folder.mkdir(exist_ok=True)

    output_path = data_folder / "sample_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Scraped {len(data)} events. Saved to {output_path}")

from data_transformers import transform_events, export_to_csv_json

if __name__ == "__main__":
    raw_data = scrape_with_retries(max_retries=3)

    # Validate
    errors = validate_events(raw_data)
    if errors:
        print("⚠️ Validation issues found, some events skipped.")
    
    # Transform
    transformed = transform_events(raw_data)

    # Export
    json_path, csv_path = export_to_csv_json(transformed, output_folder="data")
    print(f"✅ Transformed & saved to:\n- {json_path}\n- {csv_path}")
