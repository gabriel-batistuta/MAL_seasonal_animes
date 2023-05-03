from jinja2 import Template
import pdfkit
import os
import platform

def create_pdf(animeList, season):
   
    html = '<meta http-equiv="Content-type" content="text/html; charset=utf-8"/>'

    try:
        if platform.system() == 'Windows': 
            path_wkhtmltopdf = os.popen('where wkhtmltopdf').read() 

        else:
            path_wkhtmltopdf = os.popen('which wkhtmltopdf').read() 

        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    except:
        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    with open('./templates/template.html','r') as file:
        templateString = file.read()

    cssPath = './templates/template.css'

    for anime in animeList:

        context = {
            'title':anime.title,
            'image':anime.img,
            'synopsis':anime.synopsis,
            'genres':anime.genres,
            'studios':anime.studios,
            'start_date':anime.start_date,
            'source':anime.source,
            'num_episodes':anime.num_episodes,
            'day_release':anime.day_release
        }

        template = Template(templateString)
        output_text = template.render(context)
        html += output_text

    pdfkit.from_string(html, f'./animes/animes {season}.pdf', configuration=config, css=cssPath, options={ 'enable-local-file-access': None })