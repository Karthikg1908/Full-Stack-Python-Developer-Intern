document.addEventListener('DOMContentLoaded', function() {
    function handleButtonClick (event ) {
      window.location.href = event.target.getAttribute('url');
    }
      document.getElementById('student-login-btn').addEventListener('click', handleButtonClick);
      document.getElementById('recruiter-login-btn').addEventListener('click', handleButtonClick);
      document.getElementById('start-career-btn').addEventListener('click', handleButtonClick);
   });
   
    
    