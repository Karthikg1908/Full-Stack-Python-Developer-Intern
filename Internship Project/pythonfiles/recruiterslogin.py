import sqlite3
from flask import jsonify

def check_recruiter_login(username, password):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM recruiters WHERE username = ? AND password = ?', (username, password))
    recruiter = cursor.fetchone()

    conn.close()

    if recruiter:
        return jsonify({'redirected': True, 'url': '/recruiter_home'})
    else:
        return jsonify({'redirected': False})
