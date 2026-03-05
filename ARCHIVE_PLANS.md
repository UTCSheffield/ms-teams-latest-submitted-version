# Teams Assignment Archive & UI Plans

## 1. Streamlit UI Scaffold
- File: streamlit_app.py
- Features:
  - Team selection (sticky deselection)
  - Output location picker
  - Mode toggle (links/archive)
  - Date range and student filter
  - Progress bar and status display

## 2. Teams List Integration Plan
- Use Microsoft Graph API to fetch user's Teams list for selection.
- Requires Azure AD app registration (delegated permissions).
- No admin consent needed for personal Teams, but app registration may be restricted by IT.

## 3. Archive and Linking Logic
- Archive latest version of every assignment for every student in every accessible Team.
- Option to copy files locally or create links (.url files).
- Organization: by student/team/assignment (copies) and team/assignment/team (links).
- Handles version changes by replacing files in the archive.

## 4. Permissions and Limitations
- All work scoped to Teams/sites user can access.
- No org-wide or admin permissions required for personal Teams, but Azure app registration is needed.

## 5. Next Steps (when permissions available)
- Resume UI and API integration.
- Implement file copying and linking logic.
- Add progress and filtering features.

---

Stash this file in your repo for future reference when permissions are available.