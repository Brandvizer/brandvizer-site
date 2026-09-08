/* Brandvizer: licht of donker. Standaard volgt de browser, een eigen keuze wordt onthouden. */
(function(){
  function current(){
    return document.documentElement.dataset.theme ||
      (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  function labels(t){
    document.querySelectorAll('[data-theme-toggle]').forEach(function(b){
      b.setAttribute('aria-label', t === 'dark' ? 'Zet de site in de lichte stand' : 'Zet de site in de donkere stand');
    });
  }
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('[data-theme-toggle]');
    if(!b) return;
    var next = current() === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try{ localStorage.setItem('thema', next); }catch(e){}
    labels(next);
  });
  labels(current());
})();
