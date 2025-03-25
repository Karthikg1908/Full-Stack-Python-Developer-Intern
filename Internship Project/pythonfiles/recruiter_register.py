from flask import Flask, request, jsonify
import sqlite3
def register_recruiter(username, firstname, lastname, email, password, confirmPassword, company, phone_number):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recruiters WHERE username = ?", (username,))
    recruiter = cursor.fetchone()
    if recruiter:
        conn.close()
        return jsonify({'redirected': False, 'message': 'User already exists'})
    else:
        if password == confirmPassword:
            cursor.execute('''INSERT INTO recruiters (username, first_name, last_name, email_id, password, company, phone_number)VALUES (?, ?, ?, ?, ?, ?, ?)''',(username, firstname, lastname, email, password, company, phone_number))
            conn.commit()
            conn.close()
            return jsonify({'redirected': True, 'url': '/recruiter_login'})
        else:
            return jsonify({'redirected': False, 'message': 'Passwords do not match'})
            
        
    
    
    
    
