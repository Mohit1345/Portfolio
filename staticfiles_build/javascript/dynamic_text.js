const textOptions = [
    'AI',
    'Autoamation',
    'Techy',
    'Video Editing',
    'Graphic Designing',
    'Innovative Solutions',
    'Creative Designs',
    'Self-made prompter'
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



//DYNAMIC IMAGE

// import os
// import glob


// folder_path = '/path/to/folder'


// image_files = glob.glob(os.path.join(folder_path, '*.jpg'))


// // Array of image file names
// const imageFiles = ['profile1.png', 'profile2.png', 'profile3.png'];

// // Index to keep track of the current image
// let currIndex = 0;

// // Function to change the image source
// function changeImage() {
//   const imgElement = document.getElementById('hero_img');
//   imgElement.src = `/static/images/${imageFiles[currIndex]}`;
  
//   // Increment the index or reset it to 0 if it reaches the end of the array
//   currIndex = (currIndex + 1) % imageFiles.length;
// }

// // Interval in milliseconds (e.g., 5 seconds)
// const interval = 5000;

// // Call the changeImage function initially and set the interval for subsequent changes
// changeImage();
// setInterval(changeImage, interval);


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



  