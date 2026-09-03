/* =========================================================================
   Law Office of Angela Furman, LLC — interactions (multi-page)
   Vanilla JS, dependency-free, progressive enhancement.
   NOTE: The contact form is a clearly-labeled NON-PRODUCTION stub — it
   validates but transmits nothing. Wire it to an approved secure backend
   before launch (see the submit handler).
   ========================================================================= */
(function () {
  "use strict";

  var docEl = document.documentElement;
  docEl.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  /* -------------------------------------------------- Scroll-aware header, call bar, back-to-top */
  var header = document.querySelector(".site-header");
  var callbar = document.querySelector("[data-callbar]");
  var toTop = document.querySelector(".to-top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 10);
    if (callbar) callbar.classList.toggle("show", y > 560);
    if (toTop) toTop.classList.toggle("show", y > 700);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
  });

  /* -------------------------------------------------- Mobile drawer + focus handling */
  var burger = document.querySelector(".burger");
  var drawer = document.querySelector(".drawer");
  var drawerClose = document.querySelector(".drawer__close");
  var lastFocused = null;
  function focusables(c) {
    return [].slice.call(c.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])'))
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

  /* -------------------------------------------------- Hero headline lines (reveal on load) */
  var lineEls = [].slice.call(document.querySelectorAll(".lines"));
  if (reduceMotion) { lineEls.forEach(function (el) { el.classList.add("in"); }); }
  else { requestAnimationFrame(function () { requestAnimationFrame(function () { lineEls.forEach(function (el) { el.classList.add("in"); }); }); }); }

  /* -------------------------------------------------- Scroll reveal + staggered groups */
  var revealEls = [].slice.call(document.querySelectorAll("[data-reveal], [data-stagger]"));
  if (reduceMotion || !hasIO) {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* -------------------------------------------------- Count-up stats */
  var counters = [].slice.call(document.querySelectorAll("[data-count]"));
  function countUp(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var dec = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var dur = 1400, start = null;
    function frame(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(dec);
      if (p < 1) requestAnimationFrame(frame); else el.textContent = target.toFixed(dec);
    }
    requestAnimationFrame(frame);
  }
  if (counters.length) {
    if (reduceMotion || !hasIO) {
      counters.forEach(function (el) { el.textContent = parseFloat(el.getAttribute("data-count")).toFixed(parseInt(el.getAttribute("data-decimals") || "0", 10)); });
    } else {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { if (entry.isIntersecting) { countUp(entry.target); cio.unobserve(entry.target); } });
      }, { threshold: 0.6 });
      counters.forEach(function (el) { cio.observe(el); });
    }
  }

  /* -------------------------------------------------- Subtle hero image parallax */
  var parallax = document.querySelector("[data-parallax]");
  if (parallax && !reduceMotion) {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var rect = parallax.getBoundingClientRect();
        var offset = (rect.top + rect.height / 2 - window.innerHeight / 2) * -0.05;
        parallax.style.transform = "translateY(" + offset.toFixed(1) + "px)";
        ticking = false;
      });
    }, { passive: true });
  }

  /* -------------------------------------------------- FAQ accordion (accessible) */
  [].slice.call(document.querySelectorAll(".acc__head")).forEach(function (head) {
    head.addEventListener("click", function () {
      var item = head.closest(".acc__item");
      var body = document.getElementById(head.getAttribute("aria-controls"));
      var isOpen = head.getAttribute("aria-expanded") === "true";
      var container = item.parentElement;
      [].slice.call(container.querySelectorAll(".acc__head[aria-expanded='true']")).forEach(function (h) {
        if (h !== head) { h.setAttribute("aria-expanded", "false"); var b = document.getElementById(h.getAttribute("aria-controls")); if (b) b.style.height = "0px"; }
      });
      if (isOpen) { head.setAttribute("aria-expanded", "false"); body.style.height = "0px"; }
      else { head.setAttribute("aria-expanded", "true"); body.style.height = body.scrollHeight + "px"; }
    });
  });
  var resizeT;
  window.addEventListener("resize", function () {
    clearTimeout(resizeT);
    resizeT = setTimeout(function () {
      [].slice.call(document.querySelectorAll(".acc__head[aria-expanded='true']")).forEach(function (h) {
        var b = document.getElementById(h.getAttribute("aria-controls")); if (b) b.style.height = b.scrollHeight + "px";
      });
    }, 120);
  });

  /* -------------------------------------------------- Contact form: query-param prefill (from practice-area links) */
  var matterSelect = document.getElementById("matter");
  if (matterSelect) {
    var params = new URLSearchParams(window.location.search);
    var wanted = params.get("matter");
    if (wanted) {
      [].slice.call(matterSelect.options).forEach(function (opt) {
        if (opt.value === wanted || opt.text === wanted) matterSelect.value = opt.value;
      });
    }
  }

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
    function val(id){ var el = document.getElementById(id); return el ? el.value.trim() : ""; }
    function validate() {
      var ok = true;
      ok = setError("name", val("name") ? "" : "Please enter your name.") && ok;
      ok = setError("phone", val("phone") ? "" : "Please enter a phone number.") && ok;
      var email = val("email");
      ok = setError("email", !email ? "Please enter your email." : (emailRe.test(email) ? "" : "Please enter a valid email address.")) && ok;
      ok = setError("matter", val("matter") ? "" : "Please choose a practice area.") && ok;
      ok = setError("message", val("message") ? "" : "Please add a brief description.") && ok;
      return ok;
    }
    ["name", "phone", "email", "matter", "message"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", function () { if (el.closest(".field").classList.contains("invalid")) validate(); });
    });
    var submitBtn = form.querySelector('button[type="submit"]');
    function btnLabel(text) { var l = submitBtn && submitBtn.querySelector(".btn__label"); if (l) l.textContent = text; }
    function reenable() { if (submitBtn) { submitBtn.removeAttribute("disabled"); btnLabel("Request Consultation"); } }
    var reachLine = " please call <a class=\"link\" href=\"tel:+14106354910\">(410) 635-4910</a> or email <a class=\"link\" href=\"mailto:angela.furman@alfurmanlaw.com\">angela.furman@alfurmanlaw.com</a>.";
    function showSuccess() {
      if (status) { status.hidden = false; status.className = "form-status success"; status.textContent = "Thank you — your message has been sent. Angela reviews every inquiry personally and will be in touch."; }
      form.querySelectorAll("input, textarea, select, button").forEach(function (el) { el.setAttribute("disabled", "disabled"); });
    }
    function showReach(msg) {
      if (status) { status.hidden = false; status.className = "form-status success"; status.innerHTML = msg + reachLine; }
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (status) { status.hidden = true; status.className = "form-status"; }
      if (!validate()) {
        if (status) { status.hidden = false; status.className = "form-status error"; status.textContent = "Please correct the highlighted fields and try again."; }
        var firstInvalid = form.querySelector(".field.invalid input, .field.invalid select, .field.invalid textarea");
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      var action = form.getAttribute("action");
      // No live endpoint configured (form kept as a demo): show a clear notice, send nothing.
      if (!action || action === "#" || action === "") {
        showReach("Thanks — your details look complete. This form isn't connected to a live inbox yet, so to reach the firm now");
        return;
      }

      // Real submission — works with Netlify Forms (action="/") or any provider
      // (Formspree, etc.) whose endpoint you set as the form's action.
      if (submitBtn) { submitBtn.setAttribute("disabled", "disabled"); btnLabel("Sending…"); }
      var body = new URLSearchParams(new FormData(form)).toString();
      fetch(action, { method: "POST", headers: { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }, body: body })
        .then(function (r) { if (r.ok) { showSuccess(); } else { reenable(); showReach("Your message is ready. To make sure it reaches Angela right away,"); } })
        .catch(function () { reenable(); showReach("Your message is ready. To make sure it reaches Angela right away,"); });
    });
  }

  /* -------------------------------------------------- Print (consultation checklist) */
  var printBtn = document.querySelector("[data-print]");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  /* -------------------------------------------------- Footer year */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
