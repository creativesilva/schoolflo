# PVHS Digital Media site source

Not published (GitHub Pages skips folders that start with `_`).

## Edit and rebuild pages
1. Edit English copy in `build.py`, Spanish in `es.py`.
2. Run `python3 pvhs/_src/build.py` from the repo root.
   It writes `pvhs/*.html`, `pvhs/es/*.html`, and `pvhs/admin.html`.
   If any English text has no Spanish translation, the build stops and lists it in `missing.txt`.
3. Bump `V` in `build.py` when `css/style.css` or a script changes (cache busting).

## Interest form backend: the SchoolFlo Firebase project (schoolflo.org only)
- Sign ups are saved to the Firestore collection `pvhs_interest`.
- Staff admin: https://www.schoolflo.org/pvhs/admin.html (Google sign in, creativesilva1@gmail.com only).
- `firestore.rules` here is the complete rules file for the project.
- The web app keys live in `pvhs/js/firebase-config.js`.

One time setup (https://console.firebase.google.com, signed in as creativesilva1@gmail.com):
1. Add project, name it SchoolFlo, turn Google Analytics off.
2. Build > Firestore Database > Create database, production mode, location us-west2 (Los Angeles).
3. Firestore Database > Rules: replace everything with `firestore.rules` from this folder, then Publish.
4. Build > Authentication > Get started > Google > Enable. Public facing name: SchoolFlo. Support email: creativesilva1@gmail.com.
5. Authentication > Settings > Authorized domains: add `schoolflo.org` and `www.schoolflo.org`.
6. Project settings (gear) > General > Your apps > Web (</>), nickname schoolflo.org, Register app.
   Copy the firebaseConfig values into `pvhs/js/firebase-config.js`.
