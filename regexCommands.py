import re

email_text = "a list of emails, test@gmail.com, example@hotmail.com, someone@outlook.com"

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email_text)
print(emails)

comment = "this is a comment #food #holidy #dayoff #beach "

hashtags = re.findall(r'#\w+', comment)
print(hashtags)

text = "text    with spaces    in it"

cleaned_text = re.sub(r'\s+', ' ', text).strip()
print(cleaned_text)

dates = re.findall(r'\b\d{4}-\d{2}-\d{2}|\b\d{2}/\d{2}/\d{4}|\b\d{2}-\d{2}-\d{4}', text)
print(dates)

log_data = "login from 192.168.1.100, 203.0.113.45 and 8.8.8.8."

ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', log_data)
print(ip_addresses)

data = "data with some numbers in in 3345 3332 more numbers 443 9 3325, more numbers 3323456"

numbers = re.findall(r'\d+\.?\d*', data)

print(numbers)