# src/validators.py

from typing import Dict, List

def validate_event(event: Dict) -> List[str]:
    """
    Validate a single event dictionary.
    Returns a list of validation error messages.
    If the list is empty, the event is valid.
    """

    errors = []

    # Required fields
    required_fields = ["title", "date_time", "location", "url"]

    for field in required_fields:
        if field not in event:
            errors.append(f"Missing field: {field}")
        elif not event[field] or not str(event[field]).strip():
            errors.append(f"Empty value for field: {field}")

    # URL validation (simple check)
    if "url" in event:
        if not str(event["url"]).startswith(("http://", "https://")):
            errors.append(f"Invalid URL: {event['url']}")

    # Title sanity check
    if "title" in event and len(event["title"].strip()) < 3:
        errors.append("Event title too short")

    return errors


def validate_events(events: List[Dict]) -> Dict[int, List[str]]:
    """
    Validate a list of event dictionaries.
    Returns a dictionary mapping index -> list of errors.
    Example: {0: ["Missing field: title"], 2: ["Invalid URL"]}
    """
    all_errors = {}
    for idx, event in enumerate(events):
        errors = validate_event(event)
        if errors:
            all_errors[idx] = errors
    return all_errors
