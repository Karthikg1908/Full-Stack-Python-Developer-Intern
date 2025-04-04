import sqlite3
from flask import jsonify, session
def check_student_login(usn, password):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE usn = ? AND password = ?', (usn, password))
    student = cursor.fetchone()
    if student:
        session['usn'] = usn
        session['student_name'] = student[1]
        conn.close()
        return jsonify({'redirected': True, 'url': '/student_home'})
    else:
        conn.close()
        return jsonify({'redirected': False})
    