document.addEventListener('DOMContentLoaded', function() {
    const backButton = document.getElementById('back-to-home');
    backButton.addEventListener('click', function() {
      window.location.href = '/student_home';
    }); const jobId = window.location.pathname.split('/').pop();
    fetch(`/api/job_details/${jobId}`)  
    .then(response => response.json())
      .then(job => {
        document.getElementById('jobRole').textContent = `Job Role: ${job.job_role}`;
        document.getElementById('company').textContent = `Company: ${job.company}`;
        document.getElementById('package').textContent = `Package: ${job.package}`;
        document.getElementById('jobDescription').textContent = `Job Description: ${job.job_description}`;
      }) .catch(error => {
        console.error('Error fetching job details:', error);
        document.getElementById('jobRole').textContent = 'Error fetching job details';
      });
  }
  