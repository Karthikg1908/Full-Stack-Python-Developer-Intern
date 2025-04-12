import sqlite3
from flask import jsonify, session
def update_student_password(usn, email, new_password):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE usn = ? AND email_id = ?', (usn, email))
    student = cursor.fetchone()
    if student:
        cursor.execute('UPDATE students SET password = ? WHERE usn = ?', (new_password, usn))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Password updated successfully'}), 200
    else:
        conn.close()
        return jsonify({'success': False, 'message': 'Invalid USN or Email ID'}), 404
