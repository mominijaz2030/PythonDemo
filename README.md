Functional Specification Document (FSD)

Project: PythonDemo (Django MVP) - Objective Application

Repository: https://github.com/mominijaz2030/PythonDemo

Table of Contents

Overview & Scope
Actors & Roles
Data Model (summary)
Screen 1 — Landing / Home (App Shell)
Screen 2 — User Registration / Login
Screen 3 — To‑Do List Dashboard
Screen 4 — Create / Edit Task Modal
Screen 5 — Task Filters & Bulk Actions
Screen 6 — User Profile / Settings
Screen 7 — Static Pages / About / Objectives
Non‑functional Requirements
API / URL Endpoints
Acceptance Criteria & Test Cases

-------------------------------------------xxxxxxxx---------------------xxxxxxxx.................

1. Overview & Scope
This repo is an MVP containing Django apps: todolistapp, usersapp, templates, and static assets. 
The scope of this FSD is the core flows for a simple authenticated to‑do application with user management: registration/login, CRUD for tasks, task listing, filtering, and basic settings.

2. Actors & Roles
Anonymous Visitor — can view landing/about and register/login.
Authenticated User — can create, update, delete, mark done/undone, filter tasks, manage profile.
Admin — Django admin privileges for user/task management (out of scope for UI sketches but supported by Django admin).

3. Data Model (summary)
TaskList model (todolistapp)
    task: CharField(max_length=500)
    done: BooleanField(default=False)
User — Django built-in auth.User

Picture 1 — Landing / Home (App Shell)
Display app name and short description. - Show navigation bar linking to: Home, Objectives, To‑Do (dashboard), Login, Register. - If user is authenticated, show username + Logout instead of Login/Register.

Picture 2 — User Registration / Login
Registration validates required fields and password confirmation. - Login authenticates and sets session. - CSRF protection enabled. - Passwords stored via Django’s secure hashing.

Picture 3 — To‑Do List Dashboard (Main Screen)
Show list of tasks for the logged in user, ordered by most recent or incomplete first. - Each task shows: text, done indicator, edit button, delete button, created date. - Provide Add Task input at the top (inline form) or Add Task button that opens modal. - Success and error messages displayed via Django messages framework.

Picture 4 — Create / Edit Task Modal
Modal contains textarea/input for task and Save/Cancel buttons. - Editing pre-fills the current task text. - Support AJAX submission (optional) for smoother UX.

Picture 5 — Task Filters & Bulk Actions
Provide three filter states and a search input that filters by substring. - Allow selecting multiple tasks with checkboxes and performing bulk actions (Mark Done, Delete).

Picture 6 — User Profile / Settings
Profile update endpoints validate email uniqueness and proper formats. - Password change requires current password.

Picture 7 — Static Pages / Objectives
Render Objectives content as HTML pages accessible from navbar. - Serve static images from static/images/.

Non‑functional Requirements
•	Security: Use Django CSRF, authenticate views, protect user data.
•	Performance: Page responses under 300ms for normal loads (local dev not required, but keep templates efficient).
•	Accessibility: Forms labeled, focus management for modals, sufficient color contrast.
•	Internationalization: Use Django translation hooks if needed.

API / URL Endpoints (Suggested mapping)
•	GET / — Landing page
•	GET /objectives/ — Objectives documentation
•	GET /login/, POST /login/
•	GET /register/, POST /register/
•	GET /tasks/ — Dashboard (requires auth)
•	POST /tasks/add/ — Create task
•	POST /tasks/<id>/toggle/ — Toggle done
•	POST /tasks/<id>/edit/ — Update task
•	POST /tasks/<id>/delete/ — Delete task
•	POST /tasks/bulk/ — Bulk actions
•	GET/POST /profile/ — Profile settings

Acceptance Criteria & Sample Test Cases
Add Task: - Given an authenticated user, when they submit a non-empty task, then task appears in list and DB.
Toggle Done: - Given a task, when user toggles done, then DB done flips and UI updates.
Auth: - Login with invalid credentials shows an error and prevents access to /tasks/.
Delete task: - Selecting task and pressing delete shows confirmation and removes task.


