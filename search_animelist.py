import requests 
from bs4 import BeautifulSoup

class AnimeFind:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://9anime.gs/filter?keyword='
        self.adding = 'https://9anime.gs'
    def keywords_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '+'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words
    
    def search(self, keywords):
        response = requests.get(self.url+keywords, headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('a')
        return result_links 
    
    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            if search_words in text:
                href = link.get('href')
                href = self.adding + href
                send_link.add(href)
        return send_link