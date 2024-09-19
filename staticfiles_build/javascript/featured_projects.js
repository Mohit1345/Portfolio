// Function to fetch featured projects from the API
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
    // console.log(projects)
    // Get the container element for the featured projects
    const container = document.querySelector('.featured_projects');
  
    // Update the content of the container
    container.innerHTML = `

      <div class="project_title abstract "><b>${projects.name}</b></div>
      <div class="featured_desc abstract ">${projects.description}</div>
      <div class="btn featured_tags">${projects.tags}</div>
    `;
  }
  
  // Fetch the featured projects initially
  fetchFeaturedProjects();
  
  // Refresh the featured projects every 10 seconds
  setInterval(fetchFeaturedProjects, 3000);


//   <img class="featured_img" src="${projects.image}" alt="">