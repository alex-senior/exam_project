import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

url = 'https://molbuk.ua'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

text = soup.get_text()
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)

tags = [tag.name for tag in soup.find_all()]
tag_count = Counter(tags)

links = soup.find_all('a')
link_count = len(links)

images = soup.find_all('img')
image_count = len(images)

print("Частота появи слів:", word_count.most_common(10))
print("\nЧастота появи HTML-тегів:", tag_count)
print("\nКількість посилань:", link_count)
print("\nКількість зображень:", image_count)