import requests
from bs4 import BeautifulSoup

print('\nThomas is my buddy!\n')

def text_with_newlines(elem):
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name == 'br' or e.name == 'p':
            text += '\n'
    return text

def print_all_readings(results):
    for result in results:
        title_elem = result.find('h4')
        reading_elem = result.find('div', class_='poetry')
        print(title_elem.text)
        print(text_with_newlines(reading_elem))

def print_gospel_reading(results):
    for result in results:
        title_elem = result.find('h4')
        if "Gospel" in title_elem.text:
            reading_elem = result.find('div', class_='poetry')
            print(title_elem.text)
            print(text_with_newlines(reading_elem))

URL = 'http://www.usccb.org/bible/readings'
page = requests.get(URL, timeout=7)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='bibleReadingsWrapper')
print_gospel_reading(results) # You can choose the Gospel or full readings.
# print_all_readings(results) # Toggle the commented lines to switch.
