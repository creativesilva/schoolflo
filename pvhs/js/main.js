// PVHS Digital Media shared behavior: language switch, docking nav, phone menu, footer year.
(function () {
  var es = document.documentElement.lang === "es";
  var KEY = "pvhs-lang";

  // Language: the EN / ES switch remembers the choice, and later visits open in that language.
  // Storage can be blocked (private mode), so every read and write is wrapped.
  function getPref() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setPref(v) { try { localStorage.setItem(KEY, v); } catch (e) { /* ignore */ } }
  var links = document.querySelectorAll(".langtoggle a[data-lang]");
  links.forEach(function (a) {
    a.href = a.getAttribute("href").split(/[?#]/)[0] + location.search + location.hash; // keep ?course= and #anchors
    a.addEventListener("click", function () { setPref(a.getAttribute("data-lang")); });
  });
  var pref = getPref();
  if (links.length && pref && pref !== (es ? "es" : "en")) {
    var target = document.querySelector('.langtoggle a[data-lang="' + pref + '"]');
    if (target) { location.replace(target.href); return; }
  }

  var nav = document.querySelector(".mainnav");
  var toggle = document.querySelector(".navtoggle");
  var label = toggle && toggle.querySelector(".navtoggle-label");
  var T = es
    ? { open: "Abrir menú", close: "Cerrar menú", menu: "Menú", closeShort: "Cerrar" }
    : { open: "Open menu", close: "Close menu", menu: "Menu", closeShort: "Close" };

  // Dock: once the logo row scrolls away, the sticky teal bar shows the logo.
  var head = document.querySelector(".masthead");
  if (nav && head && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      nav.classList.toggle("docked", !e.isIntersecting && e.boundingClientRect.top < 0);
    }).observe(head);
  }

  function setMenu(open) {
    if (open) nav.style.setProperty("--menu-top", Math.max(0, nav.getBoundingClientRect().bottom) + "px");
    nav.classList.toggle("open", open);
    document.documentElement.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? T.close : T.open);
    if (label) label.textContent = open ? T.closeShort : T.menu;
  }
  if (nav && toggle) {
    toggle.addEventListener("click", function () { setMenu(!nav.classList.contains("open")); });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    window.addEventListener("resize", function () { if (window.innerWidth > 760) setMenu(false); });
  }

  // Full page menus: one in the header, one in the docked bar. Only one open at a time.
  var menus = Array.prototype.map.call(document.querySelectorAll(".staffmenu"), function (m) {
    return { btn: m.querySelector(".staffmenu-btn"), list: m.querySelector(".staffmenu-list") };
  }).filter(function (m) { return m.btn && m.list; });
  function setStaff(m, open) { m.list.hidden = !open; m.btn.setAttribute("aria-expanded", open ? "true" : "false"); }
  menus.forEach(function (m) {
    m.btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = m.list.hidden;
      menus.forEach(function (o) { setStaff(o, false); });
      setStaff(m, open);
    });
  });
  document.addEventListener("click", function (e) {
    menus.forEach(function (m) { if (!m.list.hidden && !m.list.contains(e.target)) setStaff(m, false); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    menus.forEach(function (m) { if (!m.list.hidden) { setStaff(m, false); m.btn.focus(); } });
  });
  // Close the header menu once it scrolls away, and the docked one when the bar undocks.
  if (nav && "MutationObserver" in window) {
    new MutationObserver(function () { menus.forEach(function (m) { setStaff(m, false); }); })
      .observe(nav, { attributes: true, attributeFilter: ["class"] });
  }

  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();
})();
