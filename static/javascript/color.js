const colorCombinations = [
  // {
  //   "--clr-rose": "#e11d48",
  //   "--clr-rose-light": "rgba(225,29,72,0.5)",
  //   "--clr-indigo": "#4f46e5"
  // },
  // {
  //   "--clr-rose": "rgb(150, 255, 88)",
  //   "--clr-rose-light": "rgb(90, 108, 80)",
  //   "--clr-indigo": "#a324cd"
  // },
  // {
  //   "--clr-rose": "rgb(235, 108, 22)",
  //   "--clr-rose-light": "rgb(102, 77, 60)",
  //   "--clr-indigo": "rgb(49, 26, 11)"
  // },
  // {
  //   "--clr-rose": "rgb(224, 218, 27)",
  //   "--clr-rose-light": "rgb(138, 166, 66)",
  //   "--clr-indigo": "rgb(66, 166, 94)"
  // },{
  //   "--clr-rose": "var(--clr-slate600)",
  //   "--clr-rose-light": "var(--clr-slate400)",
  //   "--clr-indigo": "var(--clr-light)"
  // },{
  //   "--clr-rose": "#81ebf5",
  //   "--clr-rose-light": "rgb(198, 246, 255)",
  //   "--clr-indigo": "var(--clr-light)"
  // }

  
    {
      "--clr-rose": "#e11d48",
      "--clr-rose-light": "rgba(225, 29, 72, 0.5)",
      "--clr-indigo": "#4f46e5"
    },
    {
      "--clr-rose": "#96ff58",
      "--clr-rose-light": "#5a6c50",
      "--clr-indigo": "#a324cd"
    },
    {
      "--clr-rose": "#eb6c16",
      "--clr-rose-light": "#d69452",
      "--clr-indigo": "#74fff6"
    },
    {
      "--clr-rose": "#e0da1b",
      "--clr-rose-light": "#8aa642",
      "--clr-indigo": "#42a65e"
    },
    {
      "--clr-rose": "var(--clr-slate600)",
      "--clr-rose-light": "var(--clr-slate400)",
      "--clr-indigo": "#ffd700"
    },
    {
      "--clr-rose": "#81ebf5",
      "--clr-rose-light": "#c6f6ff",
      "--clr-indigo":  "#87CEEB"
    }
  
  
];


//4
document.addEventListener('DOMContentLoaded', function() {
  // Check if a color theme is stored in local storage
  const storedTheme = localStorage.getItem('colorTheme');
  if (storedTheme) {
    const parsedTheme = JSON.parse(storedTheme);
    applyColors(parsedTheme);
  }

  const changeButton = document.querySelector('.changeButton');
  if (changeButton) {
    changeButton.addEventListener('click', changeTheme);
  }

  function changeTheme() {
    const randomIndex = Math.floor(Math.random() * colorCombinations.length);
    const randomColors = colorCombinations[randomIndex];

    // Store the selected color theme in local storage
    localStorage.setItem('colorTheme', JSON.stringify(randomColors));

    applyColors(randomColors);
  }

  function applyColors(colors) {
    const root = document.documentElement;

    for (const color in colors) {
      root.style.setProperty(color, colors[color]);
    }
  }
});



// DARK MODE SWITCH

document.addEventListener('DOMContentLoaded', function() {
  const darkSwitch = document.querySelector('.dark_mode');
  const abstractElements = document.querySelectorAll('.abstract');
  const text_content = document.querySelector('.text_content');

  // Check if mode is stored in local storage
  let isDarkMode = localStorage.getItem('isDarkMode') === 'true';

  // Apply initial mode
  toggleMode();

  darkSwitch.addEventListener('click', function() {
    isDarkMode = !isDarkMode;
    toggleMode();
  });

  function toggleMode() {
    const root = document.documentElement;

    const dark = "#070a13";
    const light = "#f1f5f9";
    const darkText = "#f1f5f9";
    const lightText = "#070a13";

    if (isDarkMode) {
      root.style.setProperty("--clr-dark", light);
      
    } else {
      root.style.setProperty("--clr-dark", dark);
    }
    text_content.style.color = isDarkMode ? lightText : darkText;
    // Apply text color to abstract elements
    abstractElements.forEach(function(abstract) {
      abstract.style.color = isDarkMode ? lightText : darkText;
    });

    // Store the mode in local storage
    localStorage.setItem('isDarkMode', isDarkMode);
  }
});

