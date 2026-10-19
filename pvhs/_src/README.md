# PVHS Digital Media site source

Not published (GitHub Pages skips folders that start with `_`).

## Edit and rebuild pages
1. Edit English copy in `build.py`, Spanish in `es.py`.
2. Run `python3 pvhs/_src/build.py` from the repo root.
   It writes `pvhs/*.html`, `pvhs/es/*.html`, and `pvhs/admin.html`.
   If any English text has no Spanish translation, the build stops and lists it in `missing.txt`.
3. Bump `V` in `build.py` when `css/style.css` or a script changes (cache busting).

## Interest form backend (Firebase project `lightwriterz-lwz`)
- Sign ups are saved to the Firestore collection `pvhs_interest`.
- Staff admin: https://www.schoolflo.org/pvhs/admin.html (Google sign in, creativesilva1@gmail.com only).
- `firestore.rules` here is the FULL rules file for the project (Light Writerz rules + the PVHS block).

One time setup in the Firebase console (https://console.firebase.google.com, project lightwriterz-lwz):
1. Firestore Database > Rules: replace everything with `firestore.rules` from this folder, then Publish.
2. Authentication > Settings > Authorized domains: add `schoolflo.org` and `www.schoolflo.org`.
