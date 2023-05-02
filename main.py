import MAL
from googletrans import Translator
from jsonAuth import Json

translator = Translator()

header = Json().readJson()

def main():
    MAL.createFolder()
    url, season = MAL.getCurrentSeason()
    animeList = MAL.getAnimes(url, header)
    animeList = MAL.getAnimeDetails(animeList, header, season, translator)
    MAL.create_pdf(animeList, season)

if __name__ == '__main__':
    main()