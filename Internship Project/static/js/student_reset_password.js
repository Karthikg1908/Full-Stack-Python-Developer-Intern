document.getElementById('resetPasswordBtn').addEventListener('click', function() {
    const usn = document.getElementById('usn').value;
    const email = document.getElementById('email').value;
    const newPassword = document.getElementById('new_password').value;
    if (!usn || !email || !newPassword) {
      alert("Please fill in all fields.");
      return;
    } const data = {
      usn: usn,
      email: email,
      new_password: newPassword
    }; fetch('/reset-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }, body: JSON.stringify(data)
    }) .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('Password reset successfully!');
        window.location.href = '/student_login';
        } else {
        alert('Error: ' + data.message);
        }}) .catch(error => {
      console.error('Error:', error);
      alert('An error occurred while resetting your password.');
        }
                   