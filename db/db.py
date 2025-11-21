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
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titre         TEXT,
                     description   TEXT,
                     begin         TEXT,
                     end           TEXT,
                     advance       INTEGER DEFAULT 0,
                     status        TEXT DEFAULT 'todo',
                     priority      INTEGER DEFAULT 0)  ''')
    c.execute('''CREATE TABLE IF NOT EXISTS TASKS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project INTEGER,
                    titre TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    status TEXT,
                    eta INTEGER,
                    done INTEGER DEFAULT 0 CHECK (done IN (0,1)),
                    emergency TEXT,
                    FOREIGN KEY(project) REFERENCES PROJECTS(id) ON DELETE SET NULL ON UPDATE CASCADE
                )''')
    
    return True
    

def ajouterProjets():
    try:
        conn = sqlite3.connect("myDB.db")
    except Error as e:
        print(e)
        return False
    c = conn.cursor()
    projects = [
        ("Project Alpha", "First test project", "2024-01-01", "2024-03-31", 20, "in_progress", 1),
        ("Project Beta", "Second project", "2024-02-15", "2024-04-15", 0, "todo", 2),
        ("Project Gamma", "Cleanup tasks", "2024-03-01", "2024-06-30", 50, "in_progress", 3),
    ]
    c.executemany(
        "INSERT INTO PROJECTS (titre, description, begin, end, advance, status, priority) VALUES (?, ?, ?, ?, ?, ?, ?)",
        projects
    )
    tasks = [
        (1, "Task 1 for Project Alpha", "2024-01-15", "todo", 5, "no", 0),
        (1, "Task 2 for Project Alpha", "2024-01-20", "in_progress", 3, "yes", 0),
        (2, "Task 1 for Project Beta", "2024-02-20", "todo", 2, "no", 0),
        (3, "Task 1 for Project Gamma", "2024-03-10", "done", 1, "no", 1),
    ]
    c.executemany(
        "INSERT INTO TASKS (project, titre, description, due_date, status, eta, done) VALUES (?, ?, ?, ?, ?, ?, ?)",
        tasks
    )
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
        
