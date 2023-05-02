import os
import shutil

def createFolder():
    if os.path.isdir('animes'):
        pass
    else:
        os.mkdir('animes')

def removeFolder():
    shutil.rmtree('./animes', ignore_errors=True)

if __name__ == '__main__':
    removeFolder()