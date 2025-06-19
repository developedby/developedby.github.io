 // Theme toggle functionality
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Set initial theme based on system preference or saved preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.body.classList.toggle('dark-theme', savedTheme === 'dark');
      themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
    } else {
      document.body.classList.toggle('dark-theme', prefersDarkScheme.matches);
      themeToggle.textContent = prefersDarkScheme.matches ? '☀️' : '🌙';
    }
  
    // Toggle theme when button is clicked
    themeToggle.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-theme');
      themeToggle.textContent = isDark ? '☀️' : '🌙';
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
  });