document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

  // Set initial theme based on saved preference or system preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    document.documentElement.classList.toggle('dark-theme', savedTheme === 'dark');
    themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
  } else {
    document.documentElement.classList.toggle('dark-theme', prefersDarkScheme.matches);
    themeToggle.textContent = prefersDarkScheme.matches ? '☀️' : '🌙';
  }

  // Listen for system theme changes if user hasn't chosen a theme
  if (!savedTheme) {
    prefersDarkScheme.addEventListener('change', e => {
      document.documentElement.classList.toggle('dark-theme', e.matches);
      themeToggle.textContent = e.matches ? '☀️' : '🌙';
    });
  }

  // Toggle theme when button is clicked
  themeToggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark-theme');
    themeToggle.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
});