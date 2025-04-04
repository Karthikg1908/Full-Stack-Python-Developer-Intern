document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the login form, signup button, and forgot button
    const loginForm = document.querySelector('#loginForm');
    const signupButton = document.getElementById('signupButton');
    const forgotButton = document.getElementById('forgotButton');

    // Add submit event listener to the login form
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Retrieve the values of the input fields
        const usn = document.getElementById('usn').value;
        const password = document.getElementById('password').value;

        // Send a POST request with the login data
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                usn: usn,
                password: password
            })
        })
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            if (data.redirected) {  // Check if the user is redirected
                localStorage.setItem('usn', usn);  // Store the USN in localStorage
                window.location.href = data.url;  // Redirect to the URL
            } else {
                alert('Login failed. Please check your credentials.');  // Show error alert
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Log any errors to the console
        });
    });

    // Signup button click event listener
    signupButton.addEventListener('click', function(event) {
        console.log('it is clicked');  // Log to the console
        event.preventDefault();  // Prevent the default button behavior
        window.location.href = '/student_register';  // Redirect to the signup page
    });

    // Forgot password button click event listener
    forgotButton.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default button behavior
        window.location.href = '/reset-password-page';  // Redirect to the reset password page
    });
});
