import sqlite3

def init_db():
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    # Makse sure to paste your sql create query of students inside the literals('''''')
    cursor.execute('''

    ''')
    # Makse sure to paste your sql create query of recruiters inside the literals('''''')
    cursor.execute('''

    ''')

    # Makse sure to paste your sql create query of jobs inside the literals('''''')

    cursor.execute('''


    ''')

    # Makse sure to paste your sql create query of student_applications inside the literals('''''')

    cursor.execute('''

    ''')

    conn.commit()
    conn.close()
