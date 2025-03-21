from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from database import init_db
from pythonfiles.report import generate_report
from pythonfiles.Student_reset_pass import update_student_password
from pythonfiles.rec_forgotpassword import update_password
from pythonfiles.recruiter_register import register_recruiter
from pythonfiles.create_job import add_job
from pythonfiles.recruiter_home import get_all_jobs
from pythonfiles.Student_home import apply_job, fetch_job_details, get_jobs_by_application_status
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


# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT REGISTRATION +++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT REGISTRATION ++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF RECRUITER REGISTRATION +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER REGISTRATION ++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++ CREATE JOB PAGE ++++++++++++++++++++++++++

# +++++++++++++++++++++++++++ END OF CREATE JOB PAGE ++++++++++++++++++++++++++

# +++++++++++++++++++++++++++ START OF RECRUITER LOGIN ++++++++++++++++++++++++++


# +++++++++++++++++++++++++++ END OF RECRUITER LOGIN ++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ RECRUITER HOME PAGE ++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER HOME PAGE ++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT LOGIN +++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT LOGIN +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT HOME PAGE +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT HOME PAGE +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF JOB DETAILS +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF JOB DETAILS +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF RECRUITER FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF RECRUITER FORGOT PASSWORD ++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF STUDENT FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ END OF STUDENT FORGOT PASSWORD +++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ START OF REPORT PAGE +++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++ END OF REPORT PAGE +++++++++++++++++++++++++++++

if __name__ == '__main__':
    app.run(debug=True)
