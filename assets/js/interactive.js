(function () {
  const root = document.documentElement;
  const nav = document.getElementById('site-navigation');
  const navToggle = document.querySelector('.nav-toggle');
  const themeToggle = document.getElementById('themeToggle');
  const backToTop = document.getElementById('backToTop');
  const siteHeader = document.querySelector('.site-header');
  const progressBar = document.querySelector('.page-progress span');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  function updateThemeIcon() {
    if (!themeToggle) return;
    const icon = themeToggle.querySelector('i');
    const dark = root.classList.contains('dark');
    icon.className = dark ? 'fas fa-sun' : 'fas fa-moon';
    themeToggle.setAttribute('aria-label', dark ? 'Use light mode' : 'Use dark mode');
  }
  updateThemeIcon();

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      root.classList.toggle('dark');
      const dark = root.classList.contains('dark');
      root.style.colorScheme = dark ? 'dark' : 'light';
      try { localStorage.setItem('cv-theme', dark ? 'dark' : 'light'); } catch (error) { /* Keep the visual toggle working. */ }
      updateThemeIcon();
    });
  }

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      const open = nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
  }

  document.querySelectorAll('.site-nav a').forEach(function (link) {
    const current = window.location.pathname.replace(/\/+$/, '') || '/';
    const target = new URL(link.href).pathname.replace(/\/+$/, '') || '/';
    if (current === target) link.classList.add('active');
  });

  document.querySelectorAll('.details-toggle').forEach(function (button) {
    button.addEventListener('click', function () {
      const panel = document.getElementById(button.getAttribute('aria-controls'));
      const expanded = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!expanded));
      button.textContent = expanded ? 'Show details' : 'Hide details';
      panel.hidden = expanded;
    });
  });

  document.querySelectorAll('.filter-button').forEach(function (button) {
    button.addEventListener('click', function () {
      const filter = button.dataset.filter;
      document.querySelectorAll('.filter-button').forEach(function (b) { b.classList.remove('active'); });
      button.classList.add('active');
      document.querySelectorAll('[data-category]').forEach(function (card) {
        card.hidden = filter !== 'all' && card.dataset.category !== filter;
      });
    });
  });

  let scrollFrame;
  function updateScrollEffects() {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollable > 0 ? Math.min(window.scrollY / scrollable, 1) : 0;
    if (progressBar) progressBar.style.transform = 'scaleX(' + progress + ')';
    if (backToTop) backToTop.classList.toggle('visible', window.scrollY > 500);
    if (siteHeader) siteHeader.classList.toggle('scrolled', window.scrollY > 18);
    scrollFrame = null;
  }

  window.addEventListener('scroll', function () {
    if (!scrollFrame) scrollFrame = window.requestAnimationFrame(updateScrollEffects);
  }, { passive: true });
  updateScrollEffects();
  if (backToTop) backToTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  window.addEventListener('pageshow', function (event) {
    if (event.persisted) updateScrollEffects();
  });

  if (!reducedMotion.matches && window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.content-card, .competency-card, .contact-card, .publication-item').forEach(function (card) {
      card.classList.add('interactive-card');
      card.addEventListener('pointermove', function (event) {
        const bounds = card.getBoundingClientRect();
        card.style.setProperty('--pointer-x', event.clientX - bounds.left + 'px');
        card.style.setProperty('--pointer-y', event.clientY - bounds.top + 'px');
      });
    });
  }

  document.addEventListener('visibilitychange', function () {
    root.classList.toggle('page-paused', document.hidden);
  });

  const slideshow = document.querySelector('.slideshow');
  if (slideshow) {
    const slides = Array.from(slideshow.querySelectorAll('.slide'));
    const dotsContainer = slideshow.querySelector('.slide-dots');
    let currentSlide = 0;
    let timer;

    function showSlide(index) {
      currentSlide = (index + slides.length) % slides.length;
      slides.forEach(function (slide, i) { slide.classList.toggle('active', i === currentSlide); });
      dotsContainer.querySelectorAll('.slide-dot').forEach(function (dot, i) {
        dot.classList.toggle('active', i === currentSlide);
        dot.setAttribute('aria-current', i === currentSlide ? 'true' : 'false');
      });
    }

    function restartTimer() {
      window.clearInterval(timer);
      if (!reducedMotion.matches) {
        timer = window.setInterval(function () { showSlide(currentSlide + 1); }, 6500);
      }
    }

    slides.forEach(function (_, i) {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'slide-dot';
      dot.setAttribute('aria-label', 'Show photo ' + (i + 1));
      dot.addEventListener('click', function () { showSlide(i); restartTimer(); });
      dotsContainer.appendChild(dot);
    });

    slideshow.querySelector('.previous').addEventListener('click', function () { showSlide(currentSlide - 1); restartTimer(); });
    slideshow.querySelector('.next').addEventListener('click', function () { showSlide(currentSlide + 1); restartTimer(); });
    slideshow.addEventListener('mouseenter', function () { window.clearInterval(timer); });
    slideshow.addEventListener('mouseleave', restartTimer);
    showSlide(0);
    restartTimer();
  }

})();
