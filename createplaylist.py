import requests
from bs4 import BeautifulSoup

class CreatePlay:
    def create(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        l = []
        first_one = soup.find_all('ul', attrs={'class': 'lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max'})
        sep = first_one[0].text.strip().split('\t\t\n\t\n\n\n\t\n\t')
        first_song = sep[0]
        first_song_writer = sep[1].split('\n\n\n\n\n\n\n\n\n\n\n\n\t\n\t')[0]
        l.append((first_song, first_song_writer))
        song_list = [first_song]
        for tags in soup.find_all('li', attrs={'class': 'o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max'}):
            song_name = tags.text.strip().split('\t\t\n\t\n\n\n\t\n\t')[0]
            song_writer = tags.text.strip().split('\t\t\n\t\n\n\n\t\n\t')[1]
            l.append((song_name, song_writer))
            song_list.append(song_name)
        return song_list


