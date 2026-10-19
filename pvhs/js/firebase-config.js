// Firebase for the PVHS Digital Media interest form and staff admin.
// Project: the SchoolFlo Firebase project (schoolflo.org only), collection "pvhs_interest".
// These web keys are public by design; the Firestore security rules (pvhs/_src/firestore.rules)
// protect the data: anyone can submit a validated sign up, and only the program owner can read or delete them.
// Values come from Firebase console > Project settings > Your apps > Web app > SDK setup and configuration.
export const firebaseConfig = {
  apiKey: "PASTE_FROM_FIREBASE",
  authDomain: "PASTE_FROM_FIREBASE",
  projectId: "PASTE_FROM_FIREBASE",
  storageBucket: "PASTE_FROM_FIREBASE",
  messagingSenderId: "PASTE_FROM_FIREBASE",
  appId: "PASTE_FROM_FIREBASE"
};
export const SDK = "https://www.gstatic.com/firebasejs/10.12.2/";
export const OWNER = "creativesilva1@gmail.com";
export const COLLECTION = "pvhs_interest";
export const COURSES = ["Photography 1", "Photography 2", "Digital Arts 1", "Digital Arts 2"];

// The school year a student is signing up for. School starts in August, so from August on
// the "next" year is the one after the current one (Oct 2026 -> 2027-2028); from January
// through July it is the year that starts this coming August (June 2027 -> 2027-2028).
export function nextSchoolYear(d = new Date()) {
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: "America/Los_Angeles", year: "numeric", month: "numeric" })
    .formatToParts(d).map(x => [x.type, x.value]));
  const y = +p.year, m = +p.month;
  const start = m >= 8 ? y + 1 : y;
  return `${start}-${start + 1}`;
}
