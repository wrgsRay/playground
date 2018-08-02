from bs4 import BeautifulSoup as bs
import requests


def main():
    url = 'https://www.nytimes.com/'
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
    stories = soup.findAll("h2", {"class": "story-heading"})
    for i in stories:
        cleantitle = i.text.strip()
        print(cleantitle)


if __name__ == '__main__':
    main()
