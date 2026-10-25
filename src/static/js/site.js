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
  /* Automatic translation (Google). Nothing loads from Google unless the visitor picks a language. */
  var pageLang = root.lang || 'en';
  var host = location.hostname;
  var readAuto = function () {
    var m = doc.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);
    if (!m) { return null; }
    var parts = decodeURIComponent(m[1]).split('/');
    return parts[2] && parts[2] !== pageLang ? parts[2] : null;
  };
  var writeAuto = function (code) {
    var val = code ? '/' + pageLang + '/' + code : '';
    var exp = code ? '' : '; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    doc.cookie = 'googtrans=' + val + '; path=/' + exp;
    doc.cookie = 'googtrans=' + val + '; path=/; domain=' + host + exp;
  };
  var auto = readAuto();
  if (auto) {
    writeAuto(auto); // keep the source language in step with the page being viewed
    var holder = doc.createElement('div');
    holder.id = 'gt-el'; holder.hidden = true;
    doc.body.appendChild(holder);
    window.wdTranslateInit = function () {
      /* global google */
      new google.translate.TranslateElement({ pageLanguage: pageLang, autoDisplay: false }, 'gt-el');
    };
    var gs = doc.createElement('script');
    gs.src = 'https://translate.google.com/translate_a/element.js?cb=wdTranslateInit';
    gs.async = true;
    doc.head.appendChild(gs);
    root.classList.add('is-auto-translated');
    $$('[data-lang-current]').forEach(function (el) { el.textContent = auto.split('-')[0].toUpperCase(); });
    $$('[data-auto-lang="' + auto + '"]').forEach(function (b) { b.setAttribute('aria-current', 'true'); });
    $$('[data-auto-off]').forEach(function (b) { b.hidden = false; });
    $$('.lang-menu .lm-site a[aria-current]').forEach(function (a) { a.removeAttribute('aria-current'); });
  }
  $$('[data-auto-lang]').forEach(function (b) {
    b.addEventListener('click', function () {
      writeAuto(b.getAttribute('data-auto-lang'));
      location.reload();
    });
  });
  $$('[data-auto-off]').forEach(function (b) {
    b.addEventListener('click', function () { writeAuto(null); location.reload(); });
  });
  $$('[data-set-lang]').forEach(function (a) {
    a.addEventListener('click', function () { writeAuto(null); });
  });

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
})();
