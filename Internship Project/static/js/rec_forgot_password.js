document.getElementById('forgot_password_form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = {
      username: document.getElementById('username').value,
      new_password: document.getElementById('new_password').value,
      confirm_password: document.getElementById('confirm_password').value
    }; fetch('/forgot_password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    body: JSON.stringify(formData)
    }) .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('Password reset successfully!');
        window.location.href = '/recruiter_login';
      } else {
        alert('Error: ' + data.message);
      }}) .catch(error => {
      console.error('Error:', error);
      alert('An unexpected error occurred. Please try again.');
    });
  });
  