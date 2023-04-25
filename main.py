from modules import filter, pdf, searcher, folder
from googletrans import Translator
from jsonAuth import Json

translator = Translator()

headers = Json().readJson()

def main():
    folder.createFolder()
    folder.createTemplateFolder()
    url, season = filter.getCurrentSeason()
    animeList = searcher.getAnimes(url, headers)
    animeList = filter.getAnimeDetails(animeList, headers, season, translator)
    pdf.create_pdf(animeList)
    folder.removeHtmlFile()

def tests():
    anime = tester.getAnime(headers)
    tester.create_pdf(anime)

if __name__ == '__main__':
    main()