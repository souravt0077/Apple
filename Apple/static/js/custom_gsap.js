// gsap.to("#text",{
//     scrollTrigger:{
//         trigger:'#text',
//         scrub:true,
//     },
//     scale:1.2,
//     duration:2,
//     delay:2,
//     transition: 0.6,
// })

// dark mode

const darkModeKey = 'darkMode';
const darkModeToggle = document.getElementById('darkModeToggle');

// Check if dark mode is enabled
const isDarkMode = localStorage.getItem(darkModeKey) === 'true';

// Apply dark mode if enabled
if (isDarkMode) {
  document.body.classList.add('dark-mode');
  darkModeToggle.textContent = 'Light Mode';
}

function toggleDarkMode() {
  const body = document.body;
  const isDarkMode = body.classList.toggle('dark-mode');

  // Store the user's preference for dark mode
  localStorage.setItem(darkModeKey, isDarkMode);

  // Update the button text
  darkModeToggle.textContent = isDarkMode ? 'Light Mode' : 'Dark Mode';
}