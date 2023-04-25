import requests
from datetime import date
import json

class Anime:
    def __init__(self, id,title,img,alternative_titles,start_date,synopsis,nsfw,created_at,media_type, genres,start_season,day_release, source,episode_duration, picture, studios):
        self.id = id
        self.title = title
        self.img = img
        self.alternative_titles = alternative_titles
        self.start_date = start_date
        self.synopsis = synopsis
        self.nsfw = nsfw
        self.created_at = created_at
        self.media_type = media_type
        self.genres = genres
        self.start_season = start_season
        self.source = source
        self.day_release = day_release
        self.episode_duration = episode_duration
        self.picture = picture
        self.studios = studios

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

def getAnimeDetails(animeList, headers, season, translator):
    
    aniList = []

    for anime in animeList:
        url = f'https://api.myanimelist.net/v2/anime/{anime["id"]}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
        resp = json.loads(requests.get(url, headers=headers).content)
        id = resp['id']
        title = resp['title']
        img = resp['main_picture']['large']
        alternative_titles = resp['alternative_titles']['synonyms']
        start_date = resp['start_date']
        synopsis = translator.translate(resp['synopsis'], dest='pt').text
        nsfw = resp['nsfw']
        created_at = resp['created_at']
        media_type = resp['media_type']
        genres = resp['genres'][0]['name']
        start_season = str(resp['start_season']['year']) + ' ' + str(resp['start_season']['season'])
        try:
            day_release = resp['broadcast']['day_of_the_week']
        except KeyError:
            day_release = 'Unknown'
        try:
            source = resp['source']
        except KeyError:
            source = ''
        episode_duration = resp['average_episode_duration']
        try:
            picture = resp['pictures'][1]
        except IndexError:
            picture = resp['pictures'][0]
        try:
            studios = resp['studios'][0]['name']
        except:
            studios = resp['studios']
        if start_season == season:
            anime = Anime(id,title,img,alternative_titles,start_date,synopsis,nsfw,created_at,media_type, genres,start_season,day_release, source, episode_duration, picture, studios)
            aniList.append(anime)
        
    return aniList