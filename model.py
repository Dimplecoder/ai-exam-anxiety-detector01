from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_anxiety(text):
    result = classifier(text)[0]
    score = result['score']

    if score < 0.4:
        return "Low"
    elif score < 0.7:
        return "Moderate"
    else:
        return "High"