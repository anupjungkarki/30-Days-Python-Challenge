import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content
print(webpage)
