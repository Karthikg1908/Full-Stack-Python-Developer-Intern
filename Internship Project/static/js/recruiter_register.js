document.getElementById('recruiter_register').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const formData= { 
      username: document.getElementById('username').value,
      firstname: document.getElementById('firstname').value,
      lastname: document.getElementById('lastname').value,
      email: document.getElementById('email').value, 
      password: document.getElementById('password').value, 
      confirm_password: document.getElementById('confirm_password').value,
      company: document.getElementById('company').value,
      phone_number: document.getElementById('phone_number').value 
    } 
    fetch('/recruiter_register', { 
      method: 'POST', 
      headers: { 
        'Content-Type': 'application/json' ,
      },  body: JSON.stringify(formData)
   }).then(response => response.json())
      .then(data => {
          if (data.redirected) {
              alert('Recruiter registered successfully!');  
              window.location.href = data.url;
          } else {
              alert('Error: ' + data.message);
          }  }).catch(error => {
          console.error('Error:', error);
          alert('An unexpected error occurred. Please try again.');
      }); 
  });
  