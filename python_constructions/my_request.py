import requests

url = requests.get("https://github.com/AlexseyWeb?tab=repositories")
print(url.text)
print(url.status_code)
