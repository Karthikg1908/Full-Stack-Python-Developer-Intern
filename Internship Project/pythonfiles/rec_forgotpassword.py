import sqlite3
from flask import jsonify
def update_password(username, new_password):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recruiters WHERE username = ? OR email_id = ?", (username, username))
    recruiter = cursor.fetchone()
    if recruiter:
        cursor.execute("UPDATE recruiters SET password = ? WHERE username = ? OR email_id = ?", (new_password, username, username))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Password updated successfully', 'url': '/recruiter_login'})
    else:
        conn.close()
        return jsonify({'success': False, 'message': 'User not found'})
        