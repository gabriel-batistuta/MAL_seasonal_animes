import requests
import json

def getAnimes(url, headers):

    response = requests.get(url,headers=headers).content
    
    json_data = json.loads(response)

    animes = json_data['data']
    nextPage = json_data['paging']
    
    animeList = []
    
    while nextPage['next'] != None:
        for anime in animes:
            anime = anime['node']
            animeList.append(anime)
        try:
            nextPage = json_data['paging']
            json_data = requests.get(nextPage['next'],headers=headers).content
            json_data = json.loads(json_data)
            animes = json_data['data']
        except:
            break
    
    return animeList
