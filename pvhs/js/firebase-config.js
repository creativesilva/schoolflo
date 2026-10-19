// Firebase for the PVHS Digital Media interest form and staff admin.
// Uses the Light Writerz Firebase project (lightwriterz-lwz), collection "pvhs_interest".
// These web keys are public by design; the Firestore security rules protect the data:
// anyone can submit a validated sign up, and only the program owner can read or delete them.
export const firebaseConfig = {
  apiKey: "AIzaSyCry9ylESz30A2VF0oP41D9EdHReAb2FSs",
  authDomain: "lightwriterz-lwz.firebaseapp.com",
  projectId: "lightwriterz-lwz",
  storageBucket: "lightwriterz-lwz.firebasestorage.app",
  messagingSenderId: "1072039375978",
  appId: "1:1072039375978:web:6de8af70bc4e1237218613"
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
