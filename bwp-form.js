/* Formularz Better Workplace w iframe. Jedno miejsce dla calego serwisu:
   wczesniej ten sam kod byl wklejany na kazdej stronie osobno i na /zapytanie
   wisial dwa razy, wiec kazda wiadomosc od ramki byla obslugiwana podwojnie.
   Obsluguje: przekazanie kontekstu (bwp:info), auto-wysokosc (bwp:resize)
   i zdarzenie form_success do dataLayer (bwp:form-success). */
(function () {
    var BRAND = 'Daily fruits';

    window.addEventListener('message', function (event) {
        var ramka = document.getElementById('bwp-form');
        if (!ramka) return;

        var zrodlo;
        try { zrodlo = new URL(ramka.src, location.href).origin; } catch (e) { return; }
        if (event.origin !== zrodlo || event.source !== ramka.contentWindow) return;

        var dane = event.data || {};

        if (dane.type === 'bwp:request-info') {
            ramka.contentWindow.postMessage({
                type: 'bwp:info',
                url: window.location.href,
                referrer: document.referrer,
                brand: BRAND
            }, zrodlo);
            return;
        }

        if (dane.type === 'bwp:resize') {
            var h = Number(dane.height);
            if (!isFinite(h) || h < 200 || h > 5000) return;
            // Ignorujemy drgania o kilka pikseli: bez tego ramka ciagle zmieniala
            // wysokosc, przegladarka korygowala scroll i uzytkownika wyrzucalo w bok.
            if (Math.abs(h - (parseInt(ramka.style.height, 10) || 0)) < 8) return;
            ramka.style.height = h + 'px';
            return;
        }

        if (dane.type === 'bwp:form-success') {
            var payload = dane.payload || {};
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                event: 'form_success',
                formID: payload.formID || 'zapytanie',
                url: payload.url || window.location.href,
                brand: payload.brand || BRAND
            });
        }
    });
})();
