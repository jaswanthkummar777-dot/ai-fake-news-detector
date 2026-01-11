# AI Fake News Detector
# Author: Jaswanth
# This program predicts whether a news article is Fake or Real using keyword scoring

fake_keywords = ["clickbait", "shocking", "breaking", "secret", "guaranteed", "exposed"]
real_keywords = ["government", "report", "official", "research", "study", "verified"]

def analyze_news(text):
    text = text.lower()
    fake_score = 0
    real_score = 0

    for word in fake_keywords:
        if word in text:
            fake_score += 1

    for word in real_keywords:
        if word in text:
            real_score += 1

    if fake_score > real_score:
        return "🟥 Fake News"
    else:
        return "🟩 Real News"

news = input("Enter news article: ")
result = analyze_news(news)

print("\nResult:", result)
