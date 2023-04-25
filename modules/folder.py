import os
import shutil

def createFolder():
    if os.path.isdir('animes'):
        pass
    else:
        os.mkdir('animes')

def createTemplateFolder():
    if os.path.isdir('animes/templates'):
        pass
    else:
        os.mkdir('animes/templates')

def removeFolder():
    shutil.rmtree('./animes', ignore_errors=True)

def removeHtmlFile():
    path = 'animes/templates'
    shutil.rmtree(path, ignore_errors=True)

def removePdfFile():
    path = './animes'
    shutil.rmtree(path, ignore_errors=True)

removePdfFile()
