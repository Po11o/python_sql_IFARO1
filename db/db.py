import sqlite3
from sqlite3 import Error


def tables():
    try:
        conn = sqlite3.connect("myDB.db")
    except Error as e:
        print(e)
        return False
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS PROJECTS
                    (titre         text,
                     description   text )  ''')
    return True

def ajouterProjets():
    try:
        conn = sqlite3.connect("myDB.db")
    except Error as e:
        print(e)
        return False
    c = conn.cursor()
    c.execute('''INSERT INTO PROJECTS (titre, description)
                 VALUES
                     ('Mon Beau Sapin',"roi des forêts"),
                     ('fastAPI',       "j'adore"),
                     ('Master',        "en route")
                     ''')
    conn.commit()
    return True

def listeTable(table):
    try:
        conn = sqlite3.connect("myDB.db")
    except Error as e:
        print(e)
        return False
    c = conn.cursor()
    mr = f'''SELECT * FROM {table} ; '''
    c.execute(mr)
    rows = c.fetchall()
    return rows

if __name__ == '__main__':
    print(tables())
    print(ajouterProjets())
    print(listeTable("PROJECTS"))
        
