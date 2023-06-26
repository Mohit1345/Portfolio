// Get the button element
const navbarToggle = document.querySelector('.navbar-toggle');

// Get the navigation bar element
const verticalNav = document.querySelector('.vertical-nav');

// Add a click event listener to the button
navbarToggle.addEventListener('click', () => {
  // Toggle the 'navbar-open' class on the button
  navbarToggle.classList.toggle('navbar-open');

  // Toggle the display of the navigation bar
  verticalNav.classList.toggle('show');
});
