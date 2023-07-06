const textOptions = [
    'AI',
    'Autoamation',
    'Tech',
    'Video Editing',
    'Innovations',
    'Creative Designs',
  ];

  // Index of the currently displayed text
  let currentIndex = 0;

  // Function to change the text
  function changeText() {
    const textElement = document.getElementById('dynamicText');
    textElement.textContent = textOptions[currentIndex];

    // Increment the index
    currentIndex = (currentIndex + 1) % textOptions.length;
  }

  // Initial text change
  document.addEventListener('DOMContentLoaded', () => {
    changeText();
  });

  // Start changing the text automatically after 3 seconds
  setInterval(changeText, 2000);





//mohits portfolio
window.addEventListener('scroll', function() {
  var heading = document.getElementById('heading');
  var bounding = heading.getBoundingClientRect();

  if (
    bounding.top >= 0 &&
    bounding.left >= 0 &&
    bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
  ) {
    heading.style.textDecoration = 'none';
    heading.style.border='3px solid var(--clr-rose)'
  } else {
    heading.style.border = '0';
    heading.style.textDecoration = 'line-through';
  }
});



  