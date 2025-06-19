document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

  function setThemeIcon(isDark) {
    if (isDark) {
      themeIcon.className = 'fas fa-sun';
      themeToggle.setAttribute('aria-label', 'Switch to light mode');
    } else {
      themeIcon.className = 'fas fa-moon';
      themeToggle.setAttribute('aria-label', 'Switch to dark mode');
    }
  }

  // Set initial theme based on saved preference or system preference
  const savedTheme = localStorage.getItem('theme');
  let isDark;
  if (savedTheme) {
    isDark = savedTheme === 'dark';
    document.documentElement.classList.toggle('dark-theme', isDark);
    setThemeIcon(isDark);
  } else {
    isDark = prefersDarkScheme.matches;
    document.documentElement.classList.toggle('dark-theme', isDark);
    setThemeIcon(isDark);
  }

  // Listen for system theme changes if user hasn't chosen a theme
  if (!savedTheme) {
    prefersDarkScheme.addEventListener('change', e => {
      document.documentElement.classList.toggle('dark-theme', e.matches);
      setThemeIcon(e.matches);
    });
  }

  // Toggle theme when button is clicked
  themeToggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark-theme');
    setThemeIcon(isDark);
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
});