# 🧩 Functional Specification Document (FSD)

### 🧱 Project: PythonDemo (Django MVP) — Objective Application  
**Repository:** [https://github.com/mominijaz2030/PythonDemo](https://github.com/mominijaz2030/PythonDemo)

---

## 📚 Table of Contents
1. [Overview & Scope](#overview--scope)
2. [Actors & Roles](#actors--roles)
3. [Data Model (summary)](#data-model-summary)
4. [Screen 1 — Landing / Home](#screen-1--landing--home)
5. [Screen 2 — User Registration / Login](#screen-2--user-registration--login)
6. [Screen 3 — To-Do List Dashboard](#screen-3--to-do-list-dashboard)
7. [Screen 4 — Create / Edit Task Modal](#screen-4--create--edit-task-modal)
8. [Screen 5 — Task Filters & Bulk Actions](#screen-5--task-filters--bulk-actions)
9. [Screen 6 — User Profile / Settings](#screen-6--user-profile--settings)
10. [Screen 7 — Static Pages / Objectives](#screen-7--static-pages--objectives)
11. [Non-functional Requirements](#nonfunctional-requirements)
12. [API / URL Endpoints](#api--url-endpoints)
13. [Acceptance Criteria & Test Cases](#acceptance-criteria--test-cases)

---

## 🧭 Overview & Scope
This repository is an MVP containing **Django apps**: `todolistapp`, `usersapp`, templates, and static assets.  
The scope includes:
- Registration/Login  
- Task CRUD (Create, Read, Update, Delete)  
- Task listing, filtering  
- Basic user settings/profile management  

---

## 👥 Actors & Roles
| Role | Description |
|------|--------------|
| **Anonymous Visitor** | Can view landing/about and register/login. |
| **Authenticated User** | Can create, update, delete, mark done/undone, filter tasks, manage profile. |
| **Admin** | Django admin privileges for user/task management (out of scope for UI). |

---

## 🧩 Data Model (summary)
```python
# TaskList model (todolistapp)
class TaskList(models.Model):
    task = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # optional


