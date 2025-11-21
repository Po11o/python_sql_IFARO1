from db.db import *
def mesProjets():
    return listeTable("PROJECTS")

if __name__ == '__main__':
    print(mesProjets())
