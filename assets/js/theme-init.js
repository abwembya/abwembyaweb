    (function () {
      var dark = false;
      try {
        var savedTheme = localStorage.getItem('cv-theme');
        dark = savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches);
      } catch (error) {
        dark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      }
      if (dark) document.documentElement.classList.add('dark');
      document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    })();
