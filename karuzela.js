/* Karuzela produktow chodzila bez przerwy, takze wtedy, gdy byla daleko poza ekranem.
   Animacja transformem jest tania, ale nie darmowa: na telefonie to staly koszt
   kompozycji i baterii przez cala dlugosc strony. Zatrzymujemy ja poza widokiem. */
(function () {
    var pas = document.querySelector('.prod-marquee');
    if (!pas || !('IntersectionObserver' in window)) return;
    pas.classList.add('stoi');
    new IntersectionObserver(function (wpisy) {
        wpisy.forEach(function (w) { pas.classList.toggle('stoi', !w.isIntersecting); });
    }, { rootMargin: '200px 0px' }).observe(pas);
})();
