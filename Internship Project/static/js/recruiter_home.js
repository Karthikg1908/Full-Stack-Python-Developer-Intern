document.addEventListener('DOMContentLoaded', function() {
    const report = document.getElementById('reports');
  
    report.addEventListener('click', function(event) {
      event.preventDefault();
      window.location.href = '/report';
    });
  
    fetch('/api/jobs')
      .then(response => response.json())
      .then(data => {
        const jobsTable = document.getElementById('jobsTable').getElementsByTagName('tbody')[0];
  
        data.forEach(job => {
          const row = jobsTable.insertRow();
          row.insertCell(0).textContent = job[0];
          row.insertCell(1).textContent = job[1];
          row.insertCell(2).textContent = job[2];
          row.insertCell(3).textContent = job[3];
  
          const descriptionCell = row.insertCell(4);
          descriptionCell.classList.add('description');
  
          const viewButton = document.createElement('button');
          viewButton.classList.add('view-btn');
          viewButton.textContent = 'View';
  
          viewButton.onclick = () => {
            window.location.href = `/recruiter/job/${job[0]}`;
          };
  
          descriptionCell.appendChild(viewButton);
        });
      });
  
    document.getElementById('create-job-btn').addEventListener('click', function() {
      window.location.href = '/create_job_page';
    });
  
    document.getElementById('logout-btn').addEventListener('click', function() {
      window.location.href = '/';
    });
  });
  