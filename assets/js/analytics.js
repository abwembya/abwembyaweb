(function () {
  'use strict';

  const id = document.currentScript && document.currentScript.dataset.analyticsId;
  if (!id || !/^G-[A-Z0-9]+$/.test(id)) return;

  const storageKey = 'abwembya.analytics.consent.v1';
  let enabled = false;

  function storedChoice() {
    try { return window.localStorage.getItem(storageKey); }
    catch (_) { return null; }
  }

  function saveChoice(choice) {
    try { window.localStorage.setItem(storageKey, choice); }
    catch (_) { /* Continue with the choice for the current page only. */ }
  }

  function startAnalytics() {
    if (enabled) return;
    enabled = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', id);
    const tag = document.createElement('script');
    tag.async = true;
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(tag);
  }

  function showPreferences() {
    if (document.getElementById('analytics-consent')) return;
    const notice = document.createElement('section');
    notice.id = 'analytics-consent';
    notice.className = 'analytics-consent';
    notice.setAttribute('role', 'region');
    notice.setAttribute('aria-label', 'Analytics privacy choices');

    const heading = document.createElement('p');
    const headingStrong = document.createElement('strong');
    headingStrong.textContent = 'Don\u2019t Panic! \ud83d\ude80';
    const source = document.createElement('em');
    source.textContent = 'The Hitchhiker\u2019s Guide to the Galaxy';
    heading.appendChild(headingStrong);
    heading.appendChild(document.createTextNode(' \u2014 '));
    heading.appendChild(source);

    const copy = document.createElement('p');
    copy.textContent = 'Welcome to my little corner of the universe! I use optional Google Analytics to understand how people explore my science and research\u2014not for advertising. Your privacy matters, and you\u2019re always in control.';

    const actions = document.createElement('div');
    actions.className = 'analytics-consent-actions';

    function choose(choice) {
      saveChoice(choice);
      notice.remove();
      if (choice === 'accepted') startAnalytics();
      else if (enabled) window.location.reload();
    }

    const decline = document.createElement('button');
    decline.type = 'button';
    decline.textContent = 'No thanks';
    decline.addEventListener('click', function () { choose('rejected'); });

    const accept = document.createElement('button');
    accept.type = 'button';
    accept.textContent = 'Sounds good!';
    accept.addEventListener('click', function () { choose('accepted'); });

    actions.appendChild(decline);
    actions.appendChild(accept);
    notice.appendChild(heading);
    notice.appendChild(copy);
    notice.appendChild(actions);
    document.body.appendChild(notice);
  }

  function initialize() {
    const preferences = document.getElementById('analytics-preferences');
    if (preferences) preferences.addEventListener('click', showPreferences);
    const choice = storedChoice();
    if (choice === 'accepted') startAnalytics();
    else if (choice !== 'rejected') showPreferences();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
})();
