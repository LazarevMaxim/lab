import requests
from bs4 import BeautifulSoup


class WebUtils:
    @staticmethod
    def download_image(url):
        r = requests.get(url, stream=True)
        data = b''
        if r.status_code == 200:
            for chunk in r.iter_content(1024):
                data += chunk
        return data

    @staticmethod
    def get_soup(url):
        print(url)
        html_text = requests.get(url, params='').text
        soup = BeautifulSoup(html_text, "lxml")
        return soup





