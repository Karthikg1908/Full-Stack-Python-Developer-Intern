import sqlite3
def get_jobs_by_application_status(usn):
    conn1 = sqlite3.connect('db/hireme.db')
    cursor1 = conn1.cursor()
    cursor1.execute(''' SELECT jobs.*, CASE WHEN student_applications.job_id IS NOT NULL THEN 'applied' ELSE 'not applied' END AS status FROM jobs LEFT JOIN student_applications ON jobs.id = student_applications.job_id AND student_applications.usn = ?''', (usn,))
    jobs = cursor1.fetchall()
    conn1.close()
    categorized_jobs = {  
        "not_applied": [dict(id=job[0], job_role=job[1], company=job[2], package=job[3], job_description=job[4]) for job in jobs if job[-1] == 'not applied'],  
        "applied": [dict(id=job[0], job_role=job[1], company=job[2], package=job[3], job_description=job[4]) for job in jobs if job[-1] == 'applied']}  
    return categorized_jobs 
def apply_job(usn, job_id):
    conn2 = sqlite3.connect('db/hireme.db')
    cursor2 = conn2.cursor()
    cursor2.execute('''INSERT INTO student_applications (usn, job_id)VALUES (?, ?)''', (usn, job_id))
    conn2.commit()
    conn2.close()
def fetch_job_details(job_id):
    conn3 = sqlite3.connect('db/hireme.db')
    cursor3 = conn3.cursor()
    cursor3.execute('SELECT * FROM jobs WHERE id =?', (job_id,))
    job = cursor3.fetchone()
    conn3.close()
    if job:
        return  {
        "job_role": job[1], 
        "company": job[2],
        "package": job[3],
        "job_description": job[4]} 
    else:
        return None 
        