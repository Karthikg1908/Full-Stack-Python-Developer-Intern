import sqlite3
def get_all_jobs():
    conn1 = sqlite3.connect('db/hireme.db')
    cursor1 = conn1.cursor()
    cursor1.execute('SELECT * FROM jobs')
    jobs = cursor1.fetchall()
    conn1.close()
    return jobs
    