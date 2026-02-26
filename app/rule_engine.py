def apply_priority_rules(event):
    if event.event_type == "security":
        return "Now", "Security override rule"
    if event.event_type == "promo":
        return "Later", "Promotional deprioritized"
    return None, None