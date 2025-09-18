import re
from datetime import datetime
import pandas as pd

def clean_whitespace(text: str) -> str:
    """Remove excessive whitespace and normalize spacing."""
    return re.sub(r"\s+", " ", text).strip() if text else text

def normalize_datetime(date_str: str) -> str:
    """
    Convert event datetime strings into standard format: %Y-%m-%d %H:%M.
    If parsing fails, return original string.
    """
    try:
        # Example: "Wednesday, September 17, 2025 · 7:00pm - 9:00pm"
        cleaned = clean_whitespace(date_str.replace("·", ""))
        parsed = datetime.strptime(cleaned.split(", ", 1)[1], "%B %d %Y %I:%M%p")
        return parsed.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return date_str

def normalize_location(location: str) -> str:
    """Standardize location naming (e.g., Online, Virtual)."""
    if not location or len(location) < 3:
        return "N/A"
    loc = location.lower()
    if "zoom" in loc or "virtual" in loc or "online" in loc:
        return "Online"
    return clean_whitespace(location)

def transform_events(events: list) -> list:
    """Apply transformations and add derived insights."""
    transformed = []
    for e in events:
        transformed.append({
            "title": clean_whitespace(e["title"]),
            "date_time": normalize_datetime(e["date_time"]),
            "location": normalize_location(e["location"]),
            "url": e["url"],
            # Example of value-added calculation
            "is_online": "Online" in normalize_location(e["location"]),
            "title_length": len(e["title"])
        })
    return transformed

def export_to_csv_json(events: list, output_folder: str = "data"):
    """Save transformed events in both CSV and JSON formats."""
    import os, json
    os.makedirs(output_folder, exist_ok=True)

    # JSON
    json_path = os.path.join(output_folder, "events_transformed.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

    # CSV
    df = pd.DataFrame(events)
    csv_path = os.path.join(output_folder, "events_transformed.csv")
    df.to_csv(csv_path, index=False)

    return json_path, csv_path
