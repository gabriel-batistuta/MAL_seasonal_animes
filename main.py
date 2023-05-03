import MAL
from googletrans import Translator
from jsonAuth import Json

translator = Translator()

header = Json().readJson()

def main(lang,season_year=None):
    MAL.createFolder()
    if season_year is not None:
        season = season_year.split(' ')[1]
        year = season_year.split(' ')[0]
        url = f'https://api.myanimelist.net/v2/anime/season/{year}/{season}'
        season = season_year
    else:
        url, season = MAL.getCurrentSeason()
    animeList = MAL.getAnimes(url, header)
    animeList = MAL.getAnimeDetails(animeList, header, season, translator, lang)
    MAL.create_pdf(animeList, season)

if __name__ == '__main__':
    lang, season_year = MAL.menu()
    if season_year != 'current':
        main(lang,season_year)
    else:
        main(lang)