document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the form element by its id
    const createJobForm = document.getElementById('createJobForm');
  
    // Add a submit event listener to the form
    createJobForm.addEventListener('submit', function(event) {
      // Prevent the default form submission
      event.preventDefault();
  
      // Retrieve form values
      const jobRole = document.getElementById('jobRole').value;
      const company = document.getElementById('company').value;
      const package = document.getElementById('package').value;
      const jobDescription = document.getElementById('jobDescription').value;
  
      // Fetch request to submit the job data
      fetch('/api/jobs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          job_role: jobRole,
          company: company,
          package: package,
          job_description: jobDescription
        })
      })
      .then(response => response.json())
      .then(data => {
        // Check if the job creation was successful
        if (data.success) {
          alert('Job created successfully');
          window.location.href = '/recruiter_home';
        } else {
          alert('Failed to create job');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  });
  