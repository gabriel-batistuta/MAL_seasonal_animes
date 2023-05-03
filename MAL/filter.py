import requests
from datetime import date
import json
from datetime import datetime

class Anime:
    def __init__(self, ani):
        self.id = ani['id']
        self.title = ani['title']
        self.img = ani['img']
        self.start_date = ani['start_date']
        self.synopsis = ani['synopsis']
        self.genres = ani['genres']
        self.start_season = ani['start_season']
        self.source = ani['source']
        self.day_release = ani['day_release']
        self.num_episodes = ani['num_episodes']
        self.studios = ani['studios']

    def __str__(self):
        if self.studios == []:
            return f'{self.title}, {self.start_season}, {self.genres}' 
        else:
            return f'{self.title}, {self.start_season}, {self.genres}, {self.studios}'

    def __repr__(self):
        return f'{self.title}, {self.start_season}, {self.genres}, {self.studios}'

def getCurrentSeason():
    
    year = date.today().strftime("%Y")
    month = date.today().strftime("%m")
    month = int(month)

    match month:
        case 1 | 2 | 3:
            season = 'WINTER'
        case 4 | 5 | 6:
            season = 'SPRING'
        case 7 | 8 | 9:
            season = 'SUMMER'
        case 10 | 11 | 12:
            season = 'FALL'
        case _:
            season = 'WINTER'
    
    
    season = season.lower()

    url = f'https://api.myanimelist.net/v2/anime/season/{year}/{season}'
    'https://api.myanimelist.net/v2/anime/season/2023/spring'

    season = year + ' ' + season

    return url, season

def getAnimeDetails(animeList, header, season, translator, lang):
    
    aniList = []

    def getDetails(url, lang):
        resp = json.loads(requests.get(url, headers=header).content)

        match(lang):
            case 'pt-br':
                synopsis = translator.translate(resp['synopsis'], dest='pt').text
                synopsis = synopsis.replace('[Escrito por MAL Rewrite]','')

                try:
                    day_release = translator.translate(resp['broadcast']['day_of_the_week'], dest='pt').text
                except KeyError:
                    day_release = 'Unknown'
                
                start_date = resp['start_date']
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                start_date = datetime.strftime(start_date,'%d/%m/%Y')

            case 'en':
                synopsis = resp['synopsis']
                synopsis = synopsis.replace('[Written by MAL Rewrite]','')

                try:
                    day_release = resp['broadcast']['day_of_the_week']
                except KeyError:
                    day_release = 'Unknown'

                start_date = resp['start_date']

            case _:
                synopsis = resp['synopsis']
                synopsis = synopsis.replace('[Written by MAL Rewrite]','')

                try:
                    day_release = resp['broadcast']['day_of_the_week']
                except KeyError:
                    day_release = 'Unknown'

                start_date = resp['start_date']

        id = resp['id']
        title = resp['title']
        img = resp['main_picture']['large']

        genres = resp['genres'][0]['name']
        start_season = str(resp['start_season']['year']) + ' ' + str(resp['start_season']['season'])

        try:
            source = resp['source']
        except KeyError:
            source = 'Unknown'

        num_episodes = resp['num_episodes']
        if num_episodes == 0 or num_episodes == '0':
            num_episodes = 'Unknown'

        try:
            studios = resp['studios'][0]['name']
        except:
            studios = resp['studios']

        if studios == []:
            studios = 'Unknown'

        ani = {
            'id':id,
            'title':title,
            'img':img,
            'start_date':start_date,
            'synopsis':synopsis,
            'genres':genres,
            'start_season':start_season,
            'day_release':day_release,
            'source':source,
            'studios':studios,
            'num_episodes':num_episodes
        }

        return ani

    for anime in animeList:
        url = f'https://api.myanimelist.net/v2/anime/{anime["id"]}?fields=id,title,main_picture,start_date,synopsis,genres,num_episodes,start_season,source,rating,studios,num_scoring_users,broadcast,average_episode_duration'

        ani = getDetails(url, lang)
        if ani['start_season'] == season:
            anime = Anime(ani)
            aniList.append(anime)
        # API failure:
        # else:
        #     title = ani['title']
        #     print(f'error: {title} not in season')
        
    return aniList