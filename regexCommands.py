import re


emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(emails)

hashtags = re.findall(r'#\w+', tweet)
print(hashtags)

cleaned_text = re.sub(r'\s+', ' ', text).strip()
print(cleaned_text)

dates = re.findall(r'\b\d{4}-\d{2}-\d{2}|\b\d{2}/\d{2}/\d{4}|\b\d{2}-\d{2}-\d{4}', text)
print(dates)