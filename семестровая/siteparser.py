from urllib.parse import quote_plus

from utils import WebUtils

#SITE_URL = 'http://www.euro-football.ru/'
#URL_GET_CLUB_ID = SITE_URL + 'team/ajax/'
#URL_GET_CLUB_INFO = SITE_URL + 'team/'

URLMASK_FIND_CLUB = 'https://www.sports.ru/search/one_box.html?how=tm&xml=yes&control_charset=%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C&query={}&search_chk=0&sname=208'
DIR_CALENDAR = 'calendar/'
DIR_TEAM = 'team/'


class ClubFactory():
    clubs_dict = {}  # cache of clubs

    @staticmethod
    def init_club(club_name):
        if club_name in ClubFactory.clubs_dict:
            return ClubFactory.clubs_dict[club_name]

        url = URLMASK_FIND_CLUB.format(quote_plus(club_name))
        soup = WebUtils.get_soup(url)

        try:
            box = soup.find('div', {'class':'overBox'})
            if '\n\r\nкоманда|Футбол\r\n' not in box.text:
                return None

            club = Club(soup)
            ClubFactory.clubs_dict[club_name] = club
            return club
        except Exception as e:
            # return None
            raise e


class Club():
    def __init__(self, soup):
        self.name = soup.a.text
        self.href = soup.a['href']
        self.team = []
        self.games = []

        self.soup = WebUtils.get_soup(self.href + DIR_TEAM)
        self.soup_calendar = WebUtils.get_soup(self.href + DIR_CALENDAR)
        self.image = None

        self.load_image()
        self.parse_info()
        self.parse_team()

    def load_image(self):
        img_href = self.soup.find('div', {'class':'img-box'}).img['src']
        self.image = WebUtils.download_image(img_href)

    def parse_info(self):
        table = self.soup_calendar.find('table', {'class': 'stat-table'}).tbody
        rows = table.findAll('tr')
        for row in rows:
            self.games.append(Game(self, row))

    def parse_team(self):
        table = self.soup.find('table', {'class': 'stat-table'}).tbody
        rows = table.findAll('tr')
        for row in rows:
            self.team.append(Player(row))

    def __str__(self):
        return '{}'.format(self.name)


class Player():
    def __init__(self, soup):
        self.name = soup.a.text
        self.href = soup.a['href']
        self.role = soup.findAll('td')[-1]['title']

    def __str__(self):
        return '{} - {}'.format(self.name, self.role)


class Game():
    def __init__(self, parent, soup):
        self.parent = parent
        self.date = soup.a.text.replace('|', ' | ').strip()
        self.contestant = soup.findAll('td')[2].a.text
        tmp = soup.findAll('td')[4]
        if 'превью' in tmp.text:
            self.score = ' - '
        else:
            self.score = tmp.b.text

    def __str__(self):
        return '{} - {} ({})'.format(self.parent.name, self.contestant, self.score)


def test():
    club = ClubFactory.init_club('цска')
    print(club)


if __name__ == '__main__':
    test()
