document.getElementById('student_register').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData= {
      usn: document.getElementById('usn').value,
      name: document.getElementById('name').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      confirm_password: document.getElementById('confirm_password').value,
      skills: document.getElementById('skills').value,
      branch: document.getElementById('branch').value,
      college_name: document.getElementById('college_name').value,
      phone_number: document.getElementById('phone_number').value 
    } 
    fetch('/student_register', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json' ,
      },  body: JSON.stringify(formData)
   }).then(response => response.json())
      .then(data => {
          if (data.redirected) {
              alert('Student registered successfully!');
              window.location.href = data.url;
          } else {
              console.log("something happened");
              alert('Error: ' + data.message);
          }  }).catch(error => {
          console.error('Error:', error);
          alert('An unexpected error occurred. Please try again.');
      }); 
  });
  