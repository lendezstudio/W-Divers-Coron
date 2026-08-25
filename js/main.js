// W Divers Coron — site scripts
(function () {
  "use strict";

  // Mobile navigation toggle
  var navToggle = document.querySelector(".nav-toggle");
  var mobileMenu = document.querySelector(".mobile-menu");

  if (navToggle && mobileMenu) {
    navToggle.addEventListener("click", function () {
      var isOpen = mobileMenu.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        mobileMenu.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Contact form: client-side only placeholder.
  // Connect the <form> action to a form backend (e.g. Formspree, Netlify Forms)
  // to receive submissions by email — see the comment near the form markup.
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      event.preventDefault();
      var status = document.getElementById("form-status");
      var required = contactForm.querySelectorAll("[required]");
      var valid = true;

      required.forEach(function (field) {
        if (!field.value.trim()) {
          valid = false;
        }
      });

      if (!valid) {
        if (status) {
          status.textContent = "Please fill in all required fields before sending.";
          status.style.color = "#d94e2f";
        }
        return;
      }

      if (status) {
        status.textContent =
          "Thanks! This form isn't yet connected to an inbox — please also reach us directly via WhatsApp, phone, or email below so your inquiry doesn't get missed.";
        status.style.color = "#1c9c8c";
      }
      contactForm.reset();
    });
  }

  // Footer year
  var yearEl = document.getElementById("current-year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // Scroll-reveal for photos. Elements are visible by default (see CSS),
  // so a failed/blocked script never leaves images hidden.
  var revealEls = document.querySelectorAll(".reveal");
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (revealEls.length && "IntersectionObserver" in window && !reduceMotion) {
    revealEls.forEach(function (el) {
      el.classList.add("reveal-pending");
    });

    var observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.remove("reveal-pending");
            entry.target.classList.add("reveal-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );

    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  }
})();
