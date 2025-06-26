import requests
from bs4 import BeautifulSoup

url = 'https://www.thehindu.com/'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

headlines = []

for a_tag in soup.find_all('a', href=True):
    text = a_tag.get_text(strip=True)
    link = a_tag['href']

    if text and len(text) > 30 and link.startswith('https://www.thehindu.com'):
        headlines.append(text)

headlines = list(set(headlines))

with open('headline.txt', 'w', encoding='utf-8') as file:
    for headline in headlines:
        print(headline)
        file.write(headline + '\n')

print("\nHeadlines saved to headlines.txt")