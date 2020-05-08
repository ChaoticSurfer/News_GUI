import requests
from bs4 import BeautifulSoup


def scrapppping():
    url = "https://www.ambebi.ge/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find_all('a')
    article_urls = []
    result = []

    for tag in tags:
        a = str(tag.get('href'))
        if a.startswith('/article'):
            article_urls.append('https://www.ambebi.ge' + a)

    for url in article_urls:
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        article_block = soup.find_all('div', {'class': 'article_block'})

        for i in article_block:
            title = str(i.find('h1').text.replace('\n', ""))
            time = i.find('div').text.replace('\n', "")
            content = i.find('div', {'class': 'article_content'}).text.strip('\n')

        result.append({'title': title, 'time': time, 'content': content})

    return result


a = scrapppping()
