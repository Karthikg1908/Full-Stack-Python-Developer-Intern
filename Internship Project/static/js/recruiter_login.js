document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('#recruiterLoginForm');
    const signupButton = document.getElementById('signupButton');
    const forgotButton = document.getElementById('forgotButton');
  
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
  
      fetch('/recruiter_login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          password: password
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.redirected) {
          window.location.href = data.url;
        } else {
          alert('Login failed. Please check your credentials.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  
    signupButton.addEventListener('click', function(event) {
      event.preventDefault();
      console.log('it is clicked');
      window.location.href = '/recruiter_register';
    });
  
    forgotButton.addEventListener('click', function(event) {
      event.preventDefault();
      window.location.href = '/rec_forgot_password';
    });
  });
  