/* =========================================================================
   Furman Family Law — interactions
   Vanilla JS, no dependencies. Progressive enhancement.
   ========================================================================= */
(function () {
  "use strict";

  var docEl = document.documentElement;
  docEl.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* -------------------------------------------------- Header scroll state */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 24) header.classList.add("is-scrolled");
    else header.classList.remove("is-scrolled");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* -------------------------------------------------- Mobile menu */
  var burger = document.querySelector(".burger");
  var mobileNav = document.querySelector(".mobile-nav");
  function closeMenu() { document.body.classList.remove("menu-open"); if (burger) burger.setAttribute("aria-expanded", "false"); }
  if (burger && mobileNav) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    mobileNav.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
  }

  /* -------------------------------------------------- Scroll reveal */
  var revealEls = [].slice.call(document.querySelectorAll("[data-reveal]"));
  var lineEls = [].slice.call(document.querySelectorAll(".reveal-lines"));

  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("in"); });
    lineEls.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });

    // hero lines reveal shortly after load
    lineEls.forEach(function (el) {
      var lio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { if (entry.isIntersecting) { entry.target.classList.add("in"); lio.unobserve(entry.target); } });
      }, { threshold: 0.2 });
      lio.observe(el);
    });
  }

  /* -------------------------------------------------- Count-up stats */
  var counters = [].slice.call(document.querySelectorAll("[data-count]"));
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var decimals = (el.getAttribute("data-decimals") | 0);
    var dur = 1400, start = null;
    function frame(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals);
      if (p < 1) requestAnimationFrame(frame);
      else el.textContent = target.toFixed(decimals);
    }
    requestAnimationFrame(frame);
  }
  if (counters.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      counters.forEach(function (el) { el.textContent = parseFloat(el.getAttribute("data-count")).toFixed(el.getAttribute("data-decimals") | 0); });
    } else {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { if (entry.isIntersecting) { animateCount(entry.target); cio.unobserve(entry.target); } });
      }, { threshold: 0.6 });
      counters.forEach(function (el) { cio.observe(el); });
    }
  }

  /* -------------------------------------------------- Generic collapse (accordion / practice list) */
  function setupCollapse(headSelector, itemSelector, bodySelector, openClass) {
    [].slice.call(document.querySelectorAll(headSelector)).forEach(function (head) {
      head.setAttribute("aria-expanded", "false");
      head.addEventListener("click", function () {
        var item = head.closest(itemSelector);
        var body = item.querySelector(bodySelector);
        var isOpen = item.classList.contains(openClass);

        // close siblings within same container
        var container = item.parentElement;
        [].slice.call(container.querySelectorAll(itemSelector)).forEach(function (sib) {
          if (sib !== item && sib.classList.contains(openClass)) {
            sib.classList.remove(openClass);
            var b = sib.querySelector(bodySelector);
            if (b) b.style.height = "0px";
            var h = sib.querySelector(headSelector);
            if (h) h.setAttribute("aria-expanded", "false");
          }
        });

        if (isOpen) {
          item.classList.remove(openClass);
          body.style.height = "0px";
          head.setAttribute("aria-expanded", "false");
        } else {
          item.classList.add(openClass);
          body.style.height = body.scrollHeight + "px";
          head.setAttribute("aria-expanded", "true");
        }
      });
    });
  }
  setupCollapse(".acc__head", ".acc__item", ".acc__body", "open");
  setupCollapse(".plist__head", ".plist__item", ".plist__body", "open");

  // keep open panels sized correctly on resize
  var resizeT;
  window.addEventListener("resize", function () {
    clearTimeout(resizeT);
    resizeT = setTimeout(function () {
      [].slice.call(document.querySelectorAll(".acc__item.open .acc__body, .plist__item.open .plist__body")).forEach(function (b) {
        b.style.height = b.scrollHeight + "px";
      });
    }, 120);
  });

  /* -------------------------------------------------- Footer year */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* -------------------------------------------------- Contact form (front-end only demo) */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector("[data-form-note]");
      if (note) {
        note.hidden = false;
        note.textContent = "Thank you — your message has been prepared. Connect this form to your intake system or email to go live.";
      }
      form.querySelectorAll("input, textarea, select, button").forEach(function (el) { el.setAttribute("disabled", "disabled"); });
    });
  }
})();
