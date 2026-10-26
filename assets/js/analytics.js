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

    const copy = document.createElement('p');
    copy.textContent = 'May I use Google Analytics to understand visits and improve this website? Analytics is optional and stays off unless you accept.';

    const actions = document.createElement('div');
    actions.className = 'analytics-consent-actions';

    function choose(choice) {
      saveChoice(choice);
      notice.remove();
      if (choice === 'accepted') startAnalytics();
    }

    const decline = document.createElement('button');
    decline.type = 'button';
    decline.textContent = 'Reject analytics';
    decline.addEventListener('click', function () { choose('rejected'); });

    const accept = document.createElement('button');
    accept.type = 'button';
    accept.textContent = 'Accept analytics';
    accept.addEventListener('click', function () { choose('accepted'); });

    actions.appendChild(decline);
    actions.appendChild(accept);
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
