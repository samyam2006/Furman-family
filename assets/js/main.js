/* =========================================================================
   Law Office of Angela Furman, LLC — interactions
   Vanilla JS, dependency-free, progressive enhancement.
   NOTE: The contact form uses a clearly-labeled NON-PRODUCTION stub.
   It does NOT transmit anything. Wire it to an approved secure backend
   or form provider before launch (see the submit handler below).
   ========================================================================= */
(function () {
  "use strict";

  var docEl = document.documentElement;
  docEl.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* -------------------------------------------------- Scroll-aware header + call bar */
  var header = document.querySelector(".site-header");
  var callbar = document.querySelector("[data-callbar]");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 24);
    if (callbar) callbar.classList.toggle("show", y > 520);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* -------------------------------------------------- Mobile drawer with focus handling */
  var burger = document.querySelector(".burger");
  var drawer = document.querySelector(".drawer");
  var drawerClose = document.querySelector(".drawer__close");
  var lastFocused = null;

  function focusables(container) {
    return [].slice.call(container.querySelectorAll('a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])'))
      .filter(function (el) { return el.offsetParent !== null; });
  }
  function openMenu() {
    lastFocused = document.activeElement;
    document.body.classList.add("menu-open");
    if (burger) burger.setAttribute("aria-expanded", "true");
    if (drawer) { drawer.setAttribute("aria-hidden", "false"); var f = focusables(drawer); if (f.length) f[0].focus(); }
  }
  function closeMenu() {
    if (!document.body.classList.contains("menu-open")) return;
    document.body.classList.remove("menu-open");
    if (burger) burger.setAttribute("aria-expanded", "false");
    if (drawer) drawer.setAttribute("aria-hidden", "true");
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }
  if (burger && drawer) {
    burger.addEventListener("click", function () {
      document.body.classList.contains("menu-open") ? closeMenu() : openMenu();
    });
    if (drawerClose) drawerClose.addEventListener("click", closeMenu);
    drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
    document.addEventListener("keydown", function (e) {
      if (!document.body.classList.contains("menu-open")) return;
      if (e.key === "Escape") { e.preventDefault(); closeMenu(); return; }
      if (e.key === "Tab") {
        var f = focusables(drawer); if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* -------------------------------------------------- Scroll reveal */
  var revealEls = [].slice.call(document.querySelectorAll("[data-reveal]"));
  var lineEls = [].slice.call(document.querySelectorAll(".reveal-lines"));
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.concat(lineEls).forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
    lineEls.forEach(function (el) { io.observe(el); });
  }

  /* -------------------------------------------------- Active section in nav */
  var navLinks = [].slice.call(document.querySelectorAll(".nav__link[href^='#']"));
  var sections = navLinks
    .map(function (l) { return document.querySelector(l.getAttribute("href")); })
    .filter(Boolean);
  if (sections.length && "IntersectionObserver" in window) {
    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.id;
          navLinks.forEach(function (l) {
            l.setAttribute("aria-current", l.getAttribute("href") === "#" + id ? "true" : "false");
          });
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });
    sections.forEach(function (s) { sio.observe(s); });
  }

  /* -------------------------------------------------- FAQ accordion (accessible) */
  [].slice.call(document.querySelectorAll(".acc__head")).forEach(function (head) {
    head.addEventListener("click", function () {
      var item = head.closest(".acc__item");
      var body = document.getElementById(head.getAttribute("aria-controls"));
      var isOpen = head.getAttribute("aria-expanded") === "true";

      // close siblings in the same accordion
      var container = item.parentElement;
      [].slice.call(container.querySelectorAll(".acc__head[aria-expanded='true']")).forEach(function (h) {
        if (h !== head) {
          h.setAttribute("aria-expanded", "false");
          var b = document.getElementById(h.getAttribute("aria-controls"));
          if (b) b.style.height = "0px";
        }
      });

      if (isOpen) { head.setAttribute("aria-expanded", "false"); body.style.height = "0px"; }
      else { head.setAttribute("aria-expanded", "true"); body.style.height = body.scrollHeight + "px"; }
    });
  });
  // keep open panel sized on resize
  var resizeT;
  window.addEventListener("resize", function () {
    clearTimeout(resizeT);
    resizeT = setTimeout(function () {
      [].slice.call(document.querySelectorAll(".acc__head[aria-expanded='true']")).forEach(function (h) {
        var b = document.getElementById(h.getAttribute("aria-controls"));
        if (b) b.style.height = b.scrollHeight + "px";
      });
    }, 120);
  });

  /* -------------------------------------------------- Practice-area → form prefill */
  [].slice.call(document.querySelectorAll(".parea__link[data-matter]")).forEach(function (link) {
    link.addEventListener("click", function () {
      var matter = link.getAttribute("data-matter");
      var select = document.getElementById("matter");
      if (select) {
        [].slice.call(select.options).forEach(function (opt) {
          if (opt.value === matter || opt.text === matter) select.value = opt.value;
        });
      }
    });
  });

  /* -------------------------------------------------- Contact form validation + NON-PRODUCTION stub */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var status = form.querySelector("[data-form-status]");

    function setError(id, msg) {
      var input = document.getElementById(id);
      var err = document.getElementById("err-" + id);
      var field = input && input.closest(".field");
      if (field) field.classList.toggle("invalid", !!msg);
      if (input) input.setAttribute("aria-invalid", msg ? "true" : "false");
      if (err) err.textContent = msg || "";
      return !msg;
    }
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function validate() {
      var ok = true;
      var name = document.getElementById("name").value.trim();
      var phone = document.getElementById("phone").value.trim();
      var email = document.getElementById("email").value.trim();
      var matter = document.getElementById("matter").value;
      var message = document.getElementById("message").value.trim();

      ok = setError("name", name ? "" : "Please enter your name.") && ok;
      ok = setError("phone", phone ? "" : "Please enter a phone number.") && ok;
      ok = setError("email", !email ? "Please enter your email." : (emailRe.test(email) ? "" : "Please enter a valid email address.")) && ok;
      ok = setError("matter", matter ? "" : "Please choose a practice area.") && ok;
      ok = setError("message", message ? "" : "Please add a brief description.") && ok;
      return ok;
    }

    // live-clear an error once the field is corrected
    ["name", "phone", "email", "matter", "message"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", function () {
        if (el.closest(".field").classList.contains("invalid")) validate();
      });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (status) { status.hidden = true; status.className = "form-status"; }

      if (!validate()) {
        if (status) {
          status.hidden = false;
          status.className = "form-status error";
          status.textContent = "Please correct the highlighted fields and try again.";
        }
        var firstInvalid = form.querySelector(".field.invalid input, .field.invalid select, .field.invalid textarea");
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      /* --------------------------------------------------------------------
         NON-PRODUCTION STUB — no data is sent anywhere.
         To go live, replace the block below with a call to an approved
         secure endpoint / form provider, e.g.:

           fetch("/api/consultation", { method: "POST", body: new FormData(form) })
             .then(...)  // show success
             .catch(...) // show failure with phone + email fallback

         Do NOT log the "message" field to analytics, console, or any
         third-party monitoring/session-replay tool.
      -------------------------------------------------------------------- */
      if (status) {
        status.hidden = false;
        status.className = "form-status success";
        status.innerHTML = "Thanks — your details look complete. This demo form isn't connected to a secure inbox yet, so to reach the firm now please call <a class=\"link\" href=\"tel:+14106354910\">(410) 635-4910</a> or email <a class=\"link\" href=\"mailto:angela.furman@alfurmanlaw.com\">angela.furman@alfurmanlaw.com</a>.";
        status.focus && status.focus();
      }
    });
  }

  /* -------------------------------------------------- Footer year */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
