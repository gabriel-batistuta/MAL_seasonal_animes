<h1 align="center">mal_seasonal_animes<h1>

**a anime seasonal getter using MAL API, this transform the data to PDF**


https://user-images.githubusercontent.com/96501194/235035549-7f758e77-2c1f-413a-b1f8-b83119355a9c.mp4


the script get data seasonal from **MAL API** and transform this in HTML to format in PDF using ***jinja2*** and ***pdfkit***

# dependencies

to download the dependencies:

- `pip install -r requirements.txt`

# running





- in *jsonAuth.py* change the value of **client_id** to your client ID from MAL API

example:
```
# your id is < 1234ABCD!@#$ >:

client_id = '1234ABCD!@#$'
```

- a secret file named '.client_ID.json' will be generated with your id

- run 'main.py' and enjoy!

# referencies:

- ***https://myanimelist.net/apiconfig/references/api/v2***

- ***https://towardsdatascience.com/how-to-easily-create-a-pdf-file-with-python-in-3-steps-a70faaf5bed5***
