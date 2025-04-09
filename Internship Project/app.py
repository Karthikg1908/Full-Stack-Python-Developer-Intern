from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from database import init_db
# from pythonfiles.report import generate_report
# from pythonfiles.Student_reset_pass import update_student_password
# from pythonfiles.rec_forgotpassword import update_password
from pythonfiles.recruiter_register import register_recruiter
from pythonfiles.create_job import add_job
# from pythonfiles.recruiter_home import get_all_jobs
# from pythonfiles.Student_home import apply_job, fetch_job_details, get_jobs_by_application_status
from pythonfiles.recruiterslogin import *
from pythonfiles.students_login import *
from pythonfiles.Students_register import register_student
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = '2345'
CORS(app)

# Initialize the database
init_db()

# Route for index page
@app.route('/')
def index():
    return render_template('index.html') 


# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT REGISTRATION +++++++++++++++++++++++++++++++
@app.route('/student_register', methods=['POST'])
def student_register():
    data = request.get_json()
    usn = data.get('usn')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirmPassword = data.get('confirm_password')
    skills = data.get('skills')
    branch = data.get('branch')
    college_name = data.get('college_name')
    phone_number = data.get('phone_number')
    return register_student(usn, name, email, password, confirmPassword, skills, branch, college_name, phone_number)
@app.route('/student_register')
def student_register_page():
    return render_template('student_register.html') 

# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT REGISTRATION ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF RECRUITER REGISTRATION +++++++++++++++++++++++++++++
@app.route("/recruiter_register", methods=['POST'])
def recruiter_register():
    data = request.get_json()
    username = data.get('username') 
    firstname = data.get('firstname') 
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    confirmPassword = data.get('confirm_password')
    company = data.get('company') 
    phone_number = data.get('phone_number')
    return register_recruiter(username, firstname, lastname, email, password, confirmPassword, company, phone_number)
@app.route('/recruiter_register')
def recruiter_register_page():
    return render_template('recruiter_register.html')
    
    
# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER REGISTRATION ++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++ CREATE JOB PAGE ++++++++++++++++++++++++++

@app.route('/api/jobs', methods=['POST'])
def api_add_job():
    data = request.get_json()
    job_role = data.get('job_role')
    company = data.get('company')
    package = data.get('package')
    job_description = data.get('job_description')
    add_job(job_role, company, package, job_description)
    return jsonify({'success': True})
    
@app.route('/create_job_page')
def create_job_page():
    return render_template('create_job.html')
    

# +++++++++++++++++++++++++++ END OF CREATE JOB PAGE ++++++++++++++++++++++++++

# +++++++++++++++++++++++++++ START OF RECRUITER LOGIN ++++++++++++++++++++++++++

@app.route('/recruiter_login', methods=['POST'])
def recruiter_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return check_recruiter_login(username, password)
    
@app.route('/recruiter_login')
def recruiter_login_page():
    return render_template('recruiter_login.html')
    

# +++++++++++++++++++++++++++ END OF RECRUITER LOGIN ++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ RECRUITER HOME PAGE ++++++++++++++++++++++++++++++

@app.route('/recruiter_home')
def recruiter_home():
    return render_template('recruiter_home.html')
    
@app.route('/recruiter/job/<int:job_id>')
def recruiter_job_page(job_id):
    return render_template('recruiter_job_details.html')
    
@app.route('/api/jobs', methods=['GET'])
def api_get_jobs():
    jobs = get_all_jobs()
    return jsonify(jobs)
    
    

# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER HOME PAGE ++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT LOGIN +++++++++++++++++++++++++++++

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usn = data.get('usn')
    password = data.get('password')
    return check_student_login(usn, password)
    
@app.route('/student_login')
def student_login():
    return render_template('student_login.html')
    


# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT LOGIN +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT HOME PAGE +++++++++++++++++++++++++++++

@app.route('/api/apply_job', methods=['POST'])

def apply_job_route():
    data = request.get_json()
    usn1 = session.get('usn')
    job_id = data.get('job_id')
    apply_job(usn1, job_id)
    return jsonify({'success': True})
    
@app.route('/student_home')
def student_home():
    return render_template('student_home.html')

@app.route('/api/jobs_by_status', methods=['GET'])
def api_get_jobs_by_status():
    usn2 = session.get('usn')
    if not usn2:
        return jsonify({'error': 'Unauthorized'}), 401
    categorized_jobs = get_jobs_by_application_status(usn2)
    return jsonify(categorized_jobs) 
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('student_login'))

@app.route('/api/job_details/<int:job_id>')
def job_details(job_id):
    job = fetch_job_details(job_id)
    if job:
        return jsonify(job)
    else:
        return jsonify({'error': 'Job not found'}), 404 
        

# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT HOME PAGE +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF JOB DETAILS +++++++++++++++++++++++++++++

@app.route('/job/<int:job_id>')
def job_page(job_id):
    return render_template('job_details.html')
    

# ++++++++++++++++++++++++++++++++++++++ END OF JOB DETAILS +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF RECRUITER FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER FORGOT PASSWORD ++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF REPORT PAGE +++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++ END OF REPORT PAGE +++++++++++++++++++++++++++++

if __name__ == '__main__':
    app.run(debug=True)
