import jinja2
import pdfkit

def create_pdf(animeList):
    # for every anime
    for anime in animeList:

        # variables for template
        context = {'title':anime.title, 'image':anime.img,'synopsis':anime.synopsis, 'genres':anime.genres, 'studios':anime.studios}

        # generate template
        with open('./template.html','r') as file:
            template = file.read()
        with open(f'./animes/templates/{anime.title}.html','x') as file:
            file.write(template)
        
        # get template and prepare using jinja2
        template_loader = jinja2.FileSystemLoader(f'./animes/templates')
        template_env = jinja2.Environment(loader=template_loader)
        templ = template_env.get_template(f'{anime.title}.html')
        output_text = templ.render(context)
        
        # transform HTML template in pdf file
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        pdfkit.from_string(output_text, f'animes/{anime.title}.pdf', configuration=config, css='./css/template.css')
        