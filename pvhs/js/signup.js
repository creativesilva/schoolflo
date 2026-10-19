// PVHS Digital Media interest form: validates, then saves one sign up to Firestore (pvhs_interest).
// Works on the English page (signup.html) and the Spanish page (es/signup.html).
import { firebaseConfig, SDK, COLLECTION, COURSES, nextSchoolYear } from "./firebase-config.js?v=1";

const es = document.documentElement.lang === "es";
const T = es ? {
  legend: y => `¿En qué grado estarás en el año escolar ${y}?`,
  name: "Escribe tu nombre y apellido.",
  sid: "Tu número de estudiante debe tener 6 dígitos.",
  grade: "Elige el grado en el que estarás.",
  course: "Elige por lo menos una clase.",
  sending: "Enviando...",
  send: "Enviar mi inscripción",
  failed: "No se pudo enviar. Revisa tu conexión a internet e inténtalo otra vez. Si sigue sin funcionar, avísale a tu maestro.",
  done: (n, c, g, y) => `Gracias, ${n}. Te inscribiste en ${c} para el año escolar ${y} (${g}.º grado).`,
  courses: { "Photography 1": "Fotografía 1", "Photography 2": "Fotografía 2", "Digital Arts 1": "Artes Digitales 1", "Digital Arts 2": "Artes Digitales 2" },
  and: " y ",
} : {
  legend: y => `What grade will you be in during the ${y} school year?`,
  name: "Please enter your first and last name.",
  sid: "Your student ID should be 6 digits.",
  grade: "Please choose the grade you will be in.",
  course: "Please choose at least one class.",
  sending: "Sending...",
  send: "Send my sign up",
  failed: "Your sign up did not send. Check your internet connection and try again. If it still does not work, let your teacher know.",
  done: (n, c, g, y) => `Thanks, ${n}. You signed up for ${c} for the ${y} school year (grade ${g}).`,
  courses: {},
  and: " and ",
};

const $ = id => document.getElementById(id);
const form = $("signupForm"), msg = $("formMsg"), btn = $("submitBtn");
const schoolYear = nextSchoolYear();
$("grade-legend").textContent = T.legend(schoolYear);

// Which page sent the student here, and which class button they pressed.
const params = new URLSearchParams(location.search);
const courseSlug = (params.get("course") || "").toLowerCase();
form.querySelectorAll('input[name="course"]').forEach(cb => { if (cb.dataset.slug === courseSlug) cb.checked = true; });
function sourcePage() {
  let from = params.get("from");
  if (!from && document.referrer) {
    try {
      const r = new URL(document.referrer);
      if (r.host === location.host && r.pathname.includes("/pvhs/")) from = r.pathname.split("/").pop().replace(/\.html$/, "") || "index";
    } catch (e) { /* ignore */ }
  }
  from = (from || "direct").replace(/[^a-z0-9-]/gi, "").slice(0, 40) || "direct";
  return courseSlug && /^[a-z0-9-]{1,20}$/.test(courseSlug) ? `${from}#${courseSlug}` : from;
}

// Load Firebase while the student fills out the form.
const fb = (async () => {
  const [{ initializeApp }, fs] = await Promise.all([import(SDK + "firebase-app.js"), import(SDK + "firebase-firestore.js")]);
  return { db: fs.getFirestore(initializeApp(firebaseConfig)), fs };
})();
fb.catch(() => {}); // reported on submit

function show(text) { msg.textContent = text; msg.hidden = !text; if (text) msg.scrollIntoView({ block: "center", behavior: "smooth" }); }
function list(items) { return items.length < 2 ? items.join("") : items.slice(0, -1).join(", ") + T.and + items[items.length - 1]; }

$("f-sid").addEventListener("input", e => { e.target.value = e.target.value.replace(/\D/g, "").slice(0, 6); });

form.addEventListener("submit", async e => {
  e.preventDefault();
  show("");
  const name = $("f-name").value.trim().replace(/\s+/g, " ");
  const sid = $("f-sid").value.trim();
  const g = form.querySelector('input[name="grade"]:checked');
  const courses = [...form.querySelectorAll('input[name="course"]:checked')].map(cb => cb.value).filter(c => COURSES.includes(c));
  const note = $("f-note").value.trim().slice(0, 500);

  if (name.length < 2 || !/\s/.test(name)) { show(T.name); $("f-name").focus(); return; }
  if (!/^[0-9]{6}$/.test(sid)) { show(T.sid); $("f-sid").focus(); return; }
  if (!g) { show(T.grade); form.querySelector('input[name="grade"]').focus(); return; }
  if (!courses.length) { show(T.course); form.querySelector('input[name="course"]').focus(); return; }

  const grade = +g.value;
  const done = () => {
    form.hidden = true;
    $("doneSummary").textContent = T.done(name.split(" ")[0], list(courses.map(c => T.courses[c] || c)), grade, schoolYear);
    $("signupDone").hidden = false;
    $("signupDone").focus();
    window.scrollTo({ top: 0, behavior: "smooth" });
  };
  if ($("f-website").value) { done(); return; } // honeypot: bots fill hidden fields

  btn.disabled = true;
  btn.textContent = T.sending;
  try {
    const { db, fs } = await fb;
    const entry = { name: name.slice(0, 80), sid, grade, schoolYear, courses, source: sourcePage(), lang: es ? "es" : "en", at: fs.serverTimestamp() };
    if (note) entry.note = note;
    await fs.addDoc(fs.collection(db, COLLECTION), entry);
    done();
  } catch (err) {
    console.error(err);
    show(T.failed);
  } finally {
    btn.disabled = false;
    btn.textContent = T.send;
  }
});
