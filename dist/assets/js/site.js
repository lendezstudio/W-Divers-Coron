/* W Divers Coron: progressive enhancements. Every page works without this file. */
(function () {
  'use strict';
  var doc = document;
  var root = doc.documentElement;
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  /* Year */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* Reveal on scroll */
  if (!reduce && hasIO) {
    root.classList.add('motion');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  }

  /* Language preference: remembered only when the visitor chooses a language */
  $$('[data-set-lang]').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('wd-lang', a.getAttribute('data-set-lang')); } catch (e) { /* storage unavailable */ }
    });
  });

  /* Language menu: close on outside click or Escape */
  var langMenus = $$('[data-lang-menu]');
  doc.addEventListener('click', function (ev) {
    langMenus.forEach(function (d) { if (d.open && !d.contains(ev.target)) { d.open = false; } });
  });
  /* Header and sticky bar: show the menu links whenever they fit on one line next to the logo and
     buttons; only when they don't (narrow screens, long languages) fall back to the Menu button */
  var fitNav = function () {
    $$('.site-header, .sticky-bar').forEach(function (bar) {
      var nav = $('.main-nav', bar), tools = $('.header-tools', bar), brand = $('.brand', bar);
      if (!nav || !tools || !brand) { return; }
      bar.classList.remove('nav-collapsed');
      if (getComputedStyle(nav).display === 'none') { return; }
      var n = nav.getBoundingClientRect(), t = tools.getBoundingClientRect(), b = brand.getBoundingClientRect();
      var rtl = doc.documentElement.dir === 'rtl';
      var room = rtl ? Math.min(n.left - t.right, b.left - n.right) : Math.min(t.left - n.right, n.left - b.right);
      if (room < 8 || n.width < 40 || t.right > window.innerWidth + 1 || t.left < -1 || doc.documentElement.scrollWidth > window.innerWidth + 1) { bar.classList.add('nav-collapsed'); }
    });
  };
  fitNav();
  window.addEventListener('resize', fitNav);
  window.addEventListener('load', fitNav);
  if (doc.fonts && doc.fonts.ready) { doc.fonts.ready.then(fitNav); }
  /* Home slideshow: crossfades every 4 s and always runs (it only rests while the tab is hidden).
     The dots jump to a slide. Without JavaScript the first slide simply stays. */
  var show = $('[data-slideshow]');
  if (show) {
    var slides = $$('[data-slide]', show);
    /* film slide: the hero text is shorter while it shows ("film-on"), and the photo row
       is sized to end just above that text */
    var setFilm = function (i) { show.classList.toggle('film-on', !!slides[i] && (slides[i].classList.contains('fit-collage') || slides[i].classList.contains('is-collage'))); if (window.fitFan) { window.fitFan(); } };
    /* top of an element relative to the slideshow, ignoring its rise-in animation */
    var restTop = function (el, base) {
      var t = el.getBoundingClientRect().top - base;
      var tf = getComputedStyle(el).transform;
      if (tf && tf !== 'none' && window.DOMMatrix) { t -= new DOMMatrix(tf).m42; }
      return t;
    };
    var fitRow = function () {
      /* film slide on computer: the photo row sits in the middle of the hero; the eyebrow,
         headline and subline sit inside its bottom-left corner, the caption inside its
         bottom-right corner, and the buttons, dots and icons below it */
      var row = $('.fit-collage .collage', show);
      var acts = $('.hero-copy .hero-actions', show);
      var sub = $('.hero-copy .hero-lines', show);
      if (!row || !acts || !sub) { return; }
      var had = show.classList.contains('film-on');
      show.classList.add('film-on');
      var sr = show.getBoundingClientRect();
      var frameH = sr.height || window.innerHeight;
      var cta = $('.site-header .header-cta');
      var cr = cta ? cta.getBoundingClientRect() : null;
      var navB = cr && cr.height ? cr.bottom - sr.top : 74;
      var gap = 24, pad = 30;
      var actTop = restTop(acts, sr.top);
      var dots0 = $('.slide-controls', show);
      if (dots0 && dots0.offsetHeight) { actTop = Math.min(actTop, restTop(dots0, sr.top)); }
      var space = Math.min(frameH - 2 * (navB + gap), 2 * (actTop - gap) - frameH);
      show.style.setProperty('--row-h', Math.max(110, space) + 'px');
      var h = row.getBoundingClientRect().height || space;
      var rowTop = Math.round((frameH - h) / 2);
      var rowBot = rowTop + h;
      show.style.setProperty('--row-top', rowTop + 'px');
      /* lift the text block so the subline ends inside the photos */
      var cur = parseFloat(getComputedStyle(acts).marginTop) || 0;
      var subBot = restTop(sub, sr.top) + sub.offsetHeight;
      show.style.setProperty('--act-mt', Math.max(16, Math.round(cur + subBot - (rowBot - pad))) + 'px');
      show.style.setProperty('--cap-b', Math.round(frameH - rowBot + pad) + 'px');
      if (!had) { show.classList.remove('film-on'); }
    };
    /* ocean design: centre the film photo strip on the hero text block */
    var rtlDir = function () { return doc.documentElement.dir === 'rtl'; };
    var fitFan = function () {
      var copy = $('.oc-copy', show);
      if (!copy) { return; }
      var r = copy.getBoundingClientRect(), sr = show.getBoundingClientRect();
      show.style.setProperty('--fan-mid', Math.round(r.top - sr.top + r.height / 2) + 'px');
      /* the slide caption sits a fixed gap under the "Explore" link */
      var plan = $('.oc-plan', show);
      if (plan) { show.style.setProperty('--cap-top', Math.round(plan.getBoundingClientRect().bottom - sr.top + 28) + 'px'); }
      /* the strip fills the room beside the text, keeping a clear gap */
      var lines = $$('.oc-copy .hero-line > *', show), edge = rtlDir() ? r.right : r.left;
      lines.forEach(function (el) { var b = el.getBoundingClientRect(); if (b.width) { edge = rtlDir() ? Math.min(edge, b.left) : Math.max(edge, b.right); } });
      var room = rtlDir() ? (edge - sr.left) - (sr.right - r.right) - 28 : (sr.right - edge) - (r.left - sr.left) - 28;
      show.style.setProperty('--fan-h', Math.max(160, Math.round((room - 16) / 2.4)) + 'px');
    };
    window.fitFan = fitFan;
    fitFan();
    window.addEventListener('resize', fitFan);
    window.addEventListener('load', fitFan);
    if (doc.fonts && doc.fonts.ready) { doc.fonts.ready.then(fitFan); }
    setFilm(0);
    fitRow();
    window.addEventListener('resize', fitRow);
    if (doc.fonts && doc.fonts.ready) { doc.fonts.ready.then(fitRow); }
    window.addEventListener('load', fitRow);
    if (window.ResizeObserver) {
      var copy = $('.hero-copy', show);
      if (copy) { new ResizeObserver(function () { fitRow(); }).observe(copy); }
    }
    var dots = $$('[data-slide-to]', show);
    var current = 0;
    var timer = null;
    var goTo = function (n) {
      current = (n + slides.length) % slides.length;
      setFilm(current);
      $$('[data-line]', show).forEach(function (ln, i) {
        var on = i === current;
        ln.classList.toggle('is-active', on);
        if (on) { ln.removeAttribute('aria-hidden'); } else { ln.setAttribute('aria-hidden', 'true'); }
      });
      slides.forEach(function (s, i) {
        var on = i === current;
        s.classList.toggle('is-active', on);
        if (on) { s.removeAttribute('aria-hidden'); } else { s.setAttribute('aria-hidden', 'true'); }
        $$('a', s).forEach(function (a) { if (on) { a.removeAttribute('tabindex'); } else { a.setAttribute('tabindex', '-1'); } });
      });
      dots.forEach(function (d, i) { if (i === current) { d.setAttribute('aria-current', 'true'); } else { d.removeAttribute('aria-current'); } });
    };
    var stop = function () { clearInterval(timer); timer = null; };
    var start = function () {
      stop();
      if (!doc.hidden && slides.length > 1) {
        timer = setInterval(function () { goTo(current + 1); }, 4000);
      }
    };
    dots.forEach(function (d) {
      d.addEventListener('click', function () { goTo(+d.getAttribute('data-slide-to')); start(); });
    });
    $$('[data-slide-step]', show).forEach(function (b) {
      b.addEventListener('click', function () { goTo(current + (+b.getAttribute('data-slide-step'))); start(); });
    });
    doc.addEventListener('visibilitychange', start);
    /* swipe on touch screens */
    var x0 = null;
    show.addEventListener('touchstart', function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
    show.addEventListener('touchend', function (ev) {
      if (x0 === null) { return; }
      var dx = ev.changedTouches[0].clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 45) { goTo(current + (dx < 0 ? 1 : -1) * (root.dir === 'rtl' ? -1 : 1)); start(); }
    });
    start();
  }

  /* Clear the cookie left by the former automatic-translation option */
  if (/(?:^|;\s*)googtrans=/.test(doc.cookie)) {
    doc.cookie = 'googtrans=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    doc.cookie = 'googtrans=; path=/; domain=' + location.hostname + '; expires=Thu, 01 Jan 1970 00:00:00 GMT';
  }

  /* Pages restored with the Back button must not reopen a stale menu */
  window.addEventListener('pageshow', function () {
    langMenus.forEach(function (d) { d.open = false; });
  });
  langMenus.forEach(function (d) {
    d.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && d.open) { d.open = false; $('summary', d).focus(); }
    });
  });

  /* Sticky bar after the framed opening */
  var bar = $('[data-sticky]');
  var opening = $('.hero, .page-open');
  if (bar && opening && hasIO) {
    var setBar = function (show) {
      bar.classList.toggle('is-visible', show);
      bar.setAttribute('aria-hidden', show ? 'false' : 'true');
      if (show) { bar.removeAttribute('inert'); } else { bar.setAttribute('inert', ''); }
      $$('a', bar).forEach(function (a) { if (show) { a.removeAttribute('tabindex'); } else { a.setAttribute('tabindex', '-1'); } });
    };
    setBar(false);
    new IntersectionObserver(function (entries) {
      setBar(!entries[0].isIntersecting);
    }, { rootMargin: '-120px 0px 0px 0px' }).observe(opening);
  }

  /* Full navigation panel */
  var panel = $('#nav-panel');
  var lastFocus = null;
  function focusables(c) {
    return $$('a[href], button:not([disabled]), summary, input, select, textarea, [tabindex]:not([tabindex="-1"])', c)
      .filter(function (el) { return el.offsetParent !== null; });
  }
  function openPanel(trigger) {
    lastFocus = trigger;
    panel.hidden = false;
    doc.body.style.overflow = 'hidden';
    $$('[data-menu-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'true'); });
    var close = $('[data-menu-close]', panel);
    if (close) { close.focus(); }
  }
  function closePanel() {
    panel.hidden = true;
    doc.body.style.overflow = '';
    $$('[data-menu-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
    if (lastFocus) { lastFocus.focus(); }
  }
  if (panel) {
    $$('[data-menu-open]').forEach(function (b) {
      b.setAttribute('role', 'button');
      b.setAttribute('aria-expanded', 'false');
      b.addEventListener('click', function (ev) { ev.preventDefault(); openPanel(b); });
      b.addEventListener('keydown', function (ev) { if (ev.key === ' ') { ev.preventDefault(); openPanel(b); } });
    });
    $('[data-menu-close]', panel).addEventListener('click', closePanel);
    panel.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') { closePanel(); return; }
      if (ev.key !== 'Tab') { return; }
      var f = focusables(panel);
      if (!f.length) { return; }
      if (ev.shiftKey && doc.activeElement === f[0]) { ev.preventDefault(); f[f.length - 1].focus(); }
      else if (!ev.shiftKey && doc.activeElement === f[f.length - 1]) { ev.preventDefault(); f[0].focus(); }
    });
    $$('a', panel).forEach(function (a) {
      a.addEventListener('click', function () { if (a.getAttribute('href').charAt(0) === '#') { closePanel(); } });
    });
  }

  /* Escape closes an open desktop submenu */
  $$('.has-sub').forEach(function (li) {
    li.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') {
        li.classList.add('sub-closed');
        $('.top', li).focus();
      }
    });
    var reopen = function () { li.classList.remove('sub-closed'); };
    li.addEventListener('mouseleave', reopen);
    li.addEventListener('focusout', function (ev) { if (!li.contains(ev.relatedTarget)) { reopen(); } });
  });

  /* Section indicators: hero rail and planning contents */
  function trackSections(links) {
    if (!hasIO || !links.length) { return; }
    var map = {};
    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var t = doc.getElementById(id);
      if (t) { map[id] = a; }
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          links.forEach(function (a) { a.removeAttribute('aria-current'); });
          var a = map[en.target.id];
          if (a) { a.setAttribute('aria-current', 'true'); }
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(map).forEach(function (id) { obs.observe(doc.getElementById(id)); });
  }
  trackSections($$('.hero-rail a'));
  trackSections($$('.toc a'));
  trackSections($$('.gal-nav a'));

  /* Filters (gallery, dive sites) */
  $$('[data-filter-group]').forEach(function (group) {
    var name = group.getAttribute('data-filter-group');
    var target = $('[data-filter-target="' + name + '"]');
    if (!target) { return; }
    $$('button', group).forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        $$('button', group).forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        $$(':scope > li', target).forEach(function (li) {
          var cats = (li.getAttribute('data-cat') || '').split(' ');
          li.hidden = !(f === 'all' || cats.indexOf(f) !== -1);
          if (!li.hidden) { li.classList.add('in'); }
        });
      });
    });
  });

  /* Gallery lightbox */
  var dlg = $('[data-lightbox-dialog]');
  if (dlg && typeof dlg.showModal === 'function') {
    var img = $('[data-lb-img]', dlg);
    var cap = $('[data-lb-cap]', dlg);
    var list = [];
    var idx = 0;
    var opener = null;
    var show = function (i) {
      idx = (i + list.length) % list.length;
      var a = list[idx];
      img.src = a.getAttribute('href');
      img.alt = a.getAttribute('data-caption') || '';
      cap.textContent = a.getAttribute('data-caption') || '';
    };
    $$('[data-lightbox]').forEach(function (a) {
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        opener = a;
        list = $$('[data-lightbox]').filter(function (x) { return !x.closest('li').hidden; });
        show(list.indexOf(a));
        dlg.showModal();
      });
    });
    $('[data-lb-prev]', dlg).addEventListener('click', function () { show(idx - 1); });
    $('[data-lb-next]', dlg).addEventListener('click', function () { show(idx + 1); });
    $('[data-lb-close]', dlg).addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowLeft') { show(idx - 1); }
      if (ev.key === 'ArrowRight') { show(idx + 1); }
    });
    dlg.addEventListener('click', function (ev) { if (ev.target === dlg) { dlg.close(); } });
    dlg.addEventListener('close', function () { img.src = 'data:,'; if (opener) { opener.focus(); } });
  }

  /* Clipboard */
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = doc.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      doc.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = doc.execCommand('copy'); } catch (e) { ok = false; }
      doc.body.removeChild(ta);
      if (ok) { resolve(); } else { reject(); }
    });
  }
  $$('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var msg = $('[data-copy-msg]');
      copyText(b.getAttribute('data-copy')).then(function () {
        if (msg) { msg.textContent = b.getAttribute('data-copied') + ': ' + b.getAttribute('data-copy'); }
      }, function () {
        if (msg) { msg.textContent = b.getAttribute('data-failed'); }
      });
    });
  });

  /* Inquiry composer: prepares a message; nothing is sent from this website */
  var form = $('[data-inquiry]');
  var cfgEl = $('[data-inquiry-config]');
  if (form && cfgEl) {
    var cfg = JSON.parse(cfgEl.textContent);
    var F = form.elements;
    var status = $('[data-status]', form);
    var summary = $('[data-err-summary]', form);
    var fallback = $('[data-copy-fallback]', form);
    var hint = $('#f-detail-hint');

    var params = new URLSearchParams(location.search);
    var interest = params.get('interest');
    if (interest && $('option[value="' + interest.replace(/[^a-z]/g, '') + '"]', F.interest)) {
      F.interest.value = interest;
    }
    var topic = params.get('topic');
    if (topic && Object.prototype.hasOwnProperty.call(cfg.topics, topic)) {
      F.topic.value = cfg.topics[topic];
      var note = doc.createElement('p');
      note.className = 'hint';
      note.textContent = cfg.labels.about + ': ' + cfg.topics[topic];
      F.message.parentNode.insertBefore(note, F.message);
    }

    var types = { email: ['email', 'email'], whatsapp: ['tel', 'tel'] };
    var setMethod = function () {
      var m = F.method.value;
      hint.textContent = cfg.hints[m] || '';
      var t = types[m] || ['text', 'off'];
      F.detail.type = t[0];
      F.detail.setAttribute('autocomplete', t[1]);
    };
    F.method.addEventListener('change', setMethod);
    setMethod();

    var fieldErr = function (el, msg) {
      var err = $('#' + el.id + '-err');
      var desc = (el.getAttribute('aria-describedby') || '').split(' ').filter(function (x) { return x && x !== err.id; });
      if (msg) {
        err.textContent = msg; err.hidden = false;
        el.setAttribute('aria-invalid', 'true');
        desc.push(err.id);
      } else {
        err.textContent = ''; err.hidden = true;
        el.removeAttribute('aria-invalid');
      }
      if (desc.length) { el.setAttribute('aria-describedby', desc.join(' ')); } else { el.removeAttribute('aria-describedby'); }
    };

    var validate = function () {
      var errs = [];
      var check = function (el, bad, msg) { fieldErr(el, bad ? msg : ''); if (bad) { errs.push([el, msg]); } };
      check(F.name, !F.name.value.trim(), cfg.errors.err_name);
      check(F.method, !F.method.value, cfg.errors.err_method);
      var d = F.detail.value.trim();
      if (!d) { check(F.detail, true, cfg.errors.err_detail); }
      else { check(F.detail, F.method.value === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d), cfg.errors.err_email); }
      check(F.interest, !F.interest.value, cfg.errors.err_interest);
      check(F.message, !F.message.value.trim(), cfg.errors.err_message);
      var ul = $('ul', summary);
      ul.innerHTML = '';
      if (errs.length) {
        errs.forEach(function (x) {
          var li = doc.createElement('li');
          var a = doc.createElement('a');
          a.href = '#' + x[0].id; a.textContent = x[1];
          a.addEventListener('click', function (ev) { ev.preventDefault(); x[0].focus(); });
          li.appendChild(a); ul.appendChild(li);
        });
        summary.hidden = false;
        summary.focus();
        return false;
      }
      summary.hidden = true;
      return true;
    };

    var optText = function (sel) { return sel.value ? sel.options[sel.selectedIndex].text : ''; };
    var compose = function () {
      var L = cfg.labels;
      var rows = [
        [L.name, F.name.value.trim()],
        [L.method, optText(F.method)],
        [L.detail, F.detail.value.trim()],
        [L.interest, optText(F.interest)],
        [L.about, F.topic.value],
        [L.dates, F.dates.value.trim()],
        [L.guests, F.guests.value.trim()],
        [L.experience, F.experience.value.trim()],
        [L.last, F.last.value.trim()],
        [L.lang, F.lang.value ? optText(F.lang) : '']
      ];
      var out = [cfg.intro, ''];
      rows.forEach(function (r) { if (r[1]) { out.push(r[0] + ': ' + r[1]); } });
      out.push('', L.message + ':', F.message.value.trim());
      return out.join('\n');
    };

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!validate()) { return; }
      window.open('https://wa.me/' + cfg.wa + '?text=' + encodeURIComponent(compose()), '_blank', 'noopener');
      status.textContent = cfg.handoff;
    });
    $('[data-action="email"]', form).addEventListener('click', function () {
      if (!validate()) { return; }
      location.href = 'mailto:' + cfg.email + '?subject=' + encodeURIComponent(cfg.subject) + '&body=' + encodeURIComponent(compose());
      status.textContent = cfg.handoff;
    });
    $('[data-action="copy"]', form).addEventListener('click', function () {
      if (!validate()) { return; }
      var text = compose();
      copyText(text).then(function () {
        fallback.hidden = true;
        status.textContent = cfg.copied;
      }, function () {
        fallback.value = text; fallback.hidden = false; fallback.select();
        status.textContent = cfg.copyFailed;
      });
    });
  }

  /* Photo grids become slideshows: one photo at a time, arrows, dots, swipe, auto-advance every 4 s */
  $$('.sg-grid').forEach(function (grid) {
    var figs = $$('.sg-fig', grid);
    if (figs.length < 2) { return; }
    var rtl = doc.documentElement.dir === 'rtl';
    grid.classList.add('sg-slider');
    var stage = doc.createElement('div'); stage.className = 'sg-stage';
    figs.forEach(function (f) { stage.appendChild(f); });
    grid.appendChild(stage);
    var prev = doc.createElement('button'), next = doc.createElement('button');
    prev.type = 'button'; next.type = 'button'; prev.className = 'sg-btn sg-prev'; next.className = 'sg-btn sg-next';
    prev.setAttribute('aria-label', 'Previous photo'); next.setAttribute('aria-label', 'Next photo');
    prev.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    next.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    stage.appendChild(prev); stage.appendChild(next);
    var count = doc.createElement('span'); count.className = 'sg-count'; count.setAttribute('aria-hidden', 'true'); stage.appendChild(count);
    ['tl', 'tr', 'bl', 'br'].forEach(function (c) { var k = doc.createElement('span'); k.className = 'sg-corner sg-' + c; k.setAttribute('aria-hidden', 'true'); stage.appendChild(k); });
    var dots = doc.createElement('div'); dots.className = 'sg-dots';
    var cur = 0, timer = null;
    var go = function (n) {
      cur = (n + figs.length) % figs.length;
      figs.forEach(function (f, i) {
        f.classList.toggle('is-on', i === cur);
        if (i === cur) { var im = $('img', f); if (im) { im.loading = 'eager'; } }
      });
      var pad = function (n) { return (n < 10 ? '0' : '') + n; };
      count.textContent = pad(cur + 1) + ' / ' + pad(figs.length);
      $$('button', dots).forEach(function (d, i) { if (i === cur) { d.setAttribute('aria-current', 'true'); } else { d.removeAttribute('aria-current'); } });
      var nx = $('img', figs[(cur + 1) % figs.length]); if (nx) { nx.loading = 'eager'; }
    };
    var restart = function () {
      clearInterval(timer);
      if (!window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        timer = setInterval(function () { if (!doc.hidden) { go(cur + 1); } }, 4000);
      }
    };
    figs.forEach(function (f, i) {
      var d = doc.createElement('button'); d.type = 'button'; d.setAttribute('aria-label', 'Photo ' + (i + 1) + ' of ' + figs.length);
      d.addEventListener('click', function () { go(i); restart(); }); dots.appendChild(d);
    });
    grid.appendChild(dots);
    prev.addEventListener('click', function () { go(cur + (rtl ? 1 : -1)); restart(); });
    next.addEventListener('click', function () { go(cur + (rtl ? -1 : 1)); restart(); });
    var x0 = null;
    stage.addEventListener('touchstart', function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', function (ev) {
      if (x0 === null) { return; }
      var dx = ev.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) { go(cur + ((dx < 0) !== rtl ? 1 : -1)); restart(); }
    });
    go(0); restart();
  });
})();
