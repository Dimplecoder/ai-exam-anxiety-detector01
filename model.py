import random

def detect_anxiety(text):

    text = text.lower()

    if "panic" in text or "scared" in text or "stress" in text:
        return "High"

    elif "nervous" in text or "worried" in text:
        return "Moderate"

    else:
        return "Low"