from modules import filter, pdf, searcher, folder
from googletrans import Translator
from jsonAuth import Json

translator = Translator()

header = Json().readJson()

def main():
    folder.createFolder()
    url, season = filter.getCurrentSeason()
    animeList = searcher.getAnimes(url, header)
    animeList = filter.getAnimeDetails(animeList, header, season, translator)
    pdf.create_pdf(animeList, season)

if __name__ == '__main__':
    main()