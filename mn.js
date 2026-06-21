/* Mobile Nav v2 — standalone, zero dependencies */
(function(){
  var burger = document.getElementById('mnBurger');
  var overlay = document.getElementById('mnOverlay');
  if(!burger || !overlay) return;

  // a11y: powiąż burger z menu i ustaw stan początkowy
  if(overlay.id) burger.setAttribute('aria-controls', overlay.id);
  burger.setAttribute('aria-expanded', 'false');

  function open(){
    burger.classList.add('active');
    overlay.classList.add('active');
    document.body.classList.add('mn-open');
    burger.setAttribute('aria-expanded', 'true');
  }
  function close(){
    burger.classList.remove('active');
    overlay.classList.remove('active');
    document.body.classList.remove('mn-open');
    burger.setAttribute('aria-expanded', 'false');
  }

  burger.addEventListener('click', function(){ overlay.classList.contains('active') ? close() : open(); });

  // Close when any link is tapped
  var links = overlay.querySelectorAll('.mn-link, .mn-cta');
  for(var i=0; i<links.length; i++){
    links[i].addEventListener('click', close);
  }

  // Close on Escape key
  document.addEventListener('keydown', function(e){ if(e.key==='Escape' && overlay.classList.contains('active')) close(); });
})();
