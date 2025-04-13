document.addEventListener('DOMContentLoaded', () => {
    const reportTable = document.querySelector('#reportTable tbody');
    const backbutton = document.getElementById('back-to-index');
    const logoutButton = document.getElementById('logout-btn');
    fetch('/api/report')
      .then(response => response.json())
      .then(data => {
        data.forEach(item => {
          const row = document.createElement('tr');
          row.innerHTML = `
          <td>${item.student_name}</td>
          <td>${item.college}</td>
          <td>${item.job_role}</td>
          <td>${item.company}</td>
          <td>${item.package}</td>
          <td>${item.status}</td>
          `; reportTable.appendChild(row);
        });}) backbutton.addEventListener('click', function(event) {
      event.preventDefault();
      window.location.href = '/recruiter_home';})
    logoutButton.addEventListener('click', function(event) {
      event.preventDefault();
      window.location.href = '/';
    });
  });
  
  