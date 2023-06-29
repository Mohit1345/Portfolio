function fetchFeaturedProjects() {
  fetch('/api/featured-projects/')
    .then(response => response.json())
    .then(data => {
      const projects = data;
      console.log(projects);
      // Update the HTML with the fetched projects
      updateFeaturedProjects(projects);
    })
    .catch(error => {
      console.error('Error fetching featured projects:', error);
    });
}

function updateFeaturedProjects(projects) {
  // Get the container element for the featured projects
  const container = document.querySelector('.featured_projects');

  // Update the content of the container
  container.innerHTML = `
    <div class="project_title abstract"><b>${projects.name}</b></div>
    <div class="featured_desc abstract">${projects.description}</div>
    <div class="btn featured_tags">${projects.tags}</div>
  `;

  // Apply dark mode font color to the updated elements
  applyDarkModeFontColor();
}

function applyDarkModeFontColor() {
  const abstractElements = document.querySelectorAll('.abstract');
  const isDarkMode = localStorage.getItem('isDarkMode') === 'true';
  const darkText = "#f1f5f9";
  const lightText = "#070a13";

  // Apply text color to abstract elements based on dark mode state
  abstractElements.forEach(function(abstract) {
    abstract.style.color = isDarkMode ? lightText : darkText;
  });
}

// Fetch the featured projects initially
fetchFeaturedProjects();

// Refresh the featured projects every 10 seconds
setInterval(fetchFeaturedProjects, 10000);
