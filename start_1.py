from bs4 import BeautifulSoup

with open('main_scraper.html', 'r') as webpage:
    content = webpage.read()
    
    soup = BeautifulSoup(content, 'lxml')
    courses_html_tags = soup.find_all('h5')
    print(courses_html_tags)
