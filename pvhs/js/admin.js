// PVHS Digital Media staff admin: Google sign-in (program owner only), sign up list,
// filters, print, CSV for Google Sheets, delete. Firestore rules enforce the owner-only access.
import { firebaseConfig, SDK, OWNER, COLLECTION, COURSES } from "./firebase-config.js?v=3";

const $ = id => document.getElementById(id);
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const PT = { timeZone: "America/Los_Angeles" };
const when = d => d ? d.toLocaleString("en-US", { ...PT, month: "short", day: "numeric", year: "numeric", hour: "numeric", minute: "2-digit" }) : "";
const SOURCES = { index: "Home page", home: "Home page", "digital-photography": "Digital Photography page", "digital-arts": "Digital Arts page",
  "fine-art": "Fine Art page", teachers: "Teachers page", signup: "Sign Up page", footer: "Footer link", direct: "Direct link" };
const sourceLabel = s => {
  const [page, course] = String(s || "direct").split("#");
  const c = { "photography-1": "Photography 1", "photography-2": "Photography 2", "digital-arts-1": "Digital Arts 1", "digital-arts-2": "Digital Arts 2", "intro-to-art": "Intro to Art", painting: "Painting" }[course];
  return (SOURCES[page] || page) + (c ? ` (${c} button)` : "");
};

let app, auth, db, A, F, rows = [];
if (String(firebaseConfig.projectId).startsWith("PASTE")) {
  $("signin").disabled = true;
  $("login-err").textContent = "Sign-in is not set up yet: the SchoolFlo Firebase project keys still need to be added to js/firebase-config.js.";
  $("login-err").hidden = false;
  throw new Error("Firebase not configured");
}
try {
  const [m1, m2, m3] = await Promise.all([import(SDK + "firebase-app.js"), import(SDK + "firebase-auth.js"), import(SDK + "firebase-firestore.js")]);
  A = m2; F = m3;
  app = m1.initializeApp(firebaseConfig);
  auth = A.getAuth(app);
  db = F.getFirestore(app);
} catch (e) {
  $("login-err").textContent = "Could not load sign-in. Check your internet connection and reload the page.";
  $("login-err").hidden = false;
  throw e;
}

$("signin").addEventListener("click", async () => {
  $("login-err").hidden = true;
  try {
    await A.signInWithPopup(auth, new A.GoogleAuthProvider().setCustomParameters({ prompt: "select_account", login_hint: OWNER }));
  } catch (e) {
    $("login-err").textContent =
      e.code === "auth/popup-closed-by-user" ? "Sign-in was closed before it finished. Please try again."
      : e.code === "auth/unauthorized-domain" ? "This website is not approved for sign-in yet. In the Firebase console, open Authentication, Settings, Authorized domains, and add www.schoolflo.org and schoolflo.org."
      : e.code === "auth/popup-blocked" ? "Your browser blocked the sign-in window. Allow pop-ups for schoolflo.org and try again."
      : "Sign-in did not finish. Please try again.";
    $("login-err").hidden = false;
  }
});
$("signout").addEventListener("click", () => A.signOut(auth));

A.onAuthStateChanged(auth, async user => {
  if (!user) { $("v-app").hidden = true; $("v-login").hidden = false; $("signout").hidden = true; return; }
  const email = (user.email || "").toLowerCase();
  if (email !== OWNER) {
    await A.signOut(auth);
    $("login-err").textContent = `${email} does not have access. Sign in with ${OWNER}.`;
    $("login-err").hidden = false;
    return;
  }
  $("who").textContent = user.displayName ? `${user.displayName} (${email})` : email;
  $("v-login").hidden = true; $("v-app").hidden = false; $("signout").hidden = false;
  await load();
});

async function load() {
  $("admin-note").textContent = "Loading sign ups...";
  try {
    const snap = await F.getDocs(F.query(F.collection(db, COLLECTION), F.orderBy("at", "desc")));
    rows = snap.docs.map(d => ({ id: d.id, ...d.data(), at: d.data().at ? d.data().at.toDate() : null }));
    const years = [...new Set(rows.map(r => r.schoolYear).filter(Boolean))].sort().reverse();
    const sel = $("flt-year"), cur = sel.value;
    sel.innerHTML = '<option value="">All years</option>' + years.map(y => `<option${y === cur ? " selected" : ""}>${esc(y)}</option>`).join("");
    $("admin-note").textContent = "";
    render();
  } catch (e) {
    console.error(e);
    $("admin-note").textContent = e.code === "permission-denied"
      ? "Permission denied. The Firestore rules for pvhs_interest have not been published yet (see the setup steps)."
      : "Could not load sign ups. Check your connection and press Refresh.";
  }
}

function filtered() {
  const c = $("flt-course").value, g = $("flt-grade").value, y = $("flt-year").value, q = $("flt-q").value.trim().toLowerCase();
  return rows.filter(r => (!c || (r.courses || []).includes(c)) && (!g || String(r.grade) === g) && (!y || r.schoolYear === y)
    && (!q || String(r.name).toLowerCase().includes(q) || String(r.sid).includes(q)));
}

function render() {
  const list = filtered();
  const bySid = rows.reduce((m, r) => (m[r.sid] = (m[r.sid] || 0) + 1, m), {});
  const count = (fn) => list.filter(fn).length;
  $("stats").innerHTML = [
    ["Sign ups", list.length],
    ...COURSES.map(c => [c, count(r => (r.courses || []).includes(c))]),
    ...[9, 10, 11, 12].map(g => [`Grade ${g}`, count(r => r.grade === g)]),
  ].map(([l, n]) => `<div><b>${n}</b><span>${esc(l)}</span></div>`).join("");
  $("rows").innerHTML = list.map(r => `<tr>
    <td>${esc(when(r.at))}</td>
    <td>${esc(r.name)}${bySid[r.sid] > 1 ? ` <span class="dup" title="This student ID signed up ${bySid[r.sid]} times">${bySid[r.sid]}x</span>` : ""}</td>
    <td>${esc(r.sid)}</td>
    <td>${esc(r.grade)}</td>
    <td>${esc(r.schoolYear)}</td>
    <td>${esc((r.courses || []).join(", "))}</td>
    <td>${esc(sourceLabel(r.source))}</td>
    <td>${esc((r.lang || "").toUpperCase())}</td>
    <td class="note-cell">${esc(r.note || "")}</td>
    <td class="no-print"><button class="del" type="button" data-id="${esc(r.id)}" aria-label="Delete sign up from ${esc(r.name)}">Delete</button></td>
  </tr>`).join("");
  $("empty").hidden = list.length > 0;
}

["flt-course", "flt-grade", "flt-year"].forEach(id => $(id).addEventListener("change", render));
$("flt-q").addEventListener("input", render);
$("btn-refresh").addEventListener("click", load);

$("rows").addEventListener("click", async e => {
  const b = e.target.closest(".del");
  if (!b) return;
  const r = rows.find(x => x.id === b.dataset.id);
  if (!r || !confirm(`Delete the sign up from ${r.name} (${r.sid})? This cannot be undone.`)) return;
  try {
    await F.deleteDoc(F.doc(db, COLLECTION, r.id));
    rows = rows.filter(x => x.id !== r.id);
    render();
  } catch (err) {
    console.error(err);
    alert("Could not delete. Please try again.");
  }
});

function filterLabel() {
  const parts = [$("flt-course").value, $("flt-grade").value && `Grade ${$("flt-grade").value}`, $("flt-year").value, $("flt-q").value.trim() && `"${$("flt-q").value.trim()}"`].filter(Boolean);
  return parts.length ? parts.join(" · ") : "All sign ups";
}

$("btn-print").addEventListener("click", () => {
  $("print-meta").textContent = `${filterLabel()} · ${filtered().length} students · Printed ${new Date().toLocaleDateString("en-US", { ...PT, month: "long", day: "numeric", year: "numeric" })}`;
  window.print();
});

// CSV opens straight in Google Sheets (File, Import) or Excel. Cells that start with = + - @
// are prefixed with ' so a spreadsheet never runs them as formulas.
$("btn-csv").addEventListener("click", () => {
  const cell = v => {
    let s = String(v ?? "");
    if (/^[=+\-@]/.test(s)) s = "'" + s;
    return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
  };
  const head = ["Submitted", "Name", "Student ID", "Grade next year", "School year", "Classes", "Signed up from", "Language", "Note"];
  const body = filtered().map(r => [when(r.at), r.name, r.sid, r.grade, r.schoolYear, (r.courses || []).join("; "), sourceLabel(r.source), (r.lang || "").toUpperCase(), r.note || ""]);
  const csv = "﻿" + [head, ...body].map(row => row.map(cell).join(",")).join("\r\n");
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
  a.download = `pvhs-digital-media-signups-${new Date().toLocaleDateString("en-CA", PT)}.csv`;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
});
