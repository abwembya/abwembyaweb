(function () {
  const analyticsID = document.currentScript.dataset.analyticsId;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', analyticsID);
})();
