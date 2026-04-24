College Event Management System (CEMS)

A **Django-based web application** to manage and explore college events efficiently.
It provides a platform where **admins can create and manage events**, and **students can view events category-wise** in a clean and interactive interface.

Features
**User Authentication**

  * Login & Register system for users
  * Secure session handling

**Admin Panel**

  * Add, edit, and delete events
  * Manage all event details from Django Admin

**Dynamic Event Management**

  * Events stored in database
  * No hardcoding — updates reflect instantly

**Category-Based Filtering**

  * Tech Fest
  * Cultural Fest
  * Sports Meet

**Modern UI**

  * Clean and responsive design
  * Smooth navigation and event cards

**Logout Functionality**

  * Secure logout with session termination

Tech Stack

Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (default Django DB)
Authentication:** Django Auth System

Setup Instructions

1. Clone the Repository

```bash
git clone <your-repo-link>
cd cems
```

2. Install Dependencies

```bash
pip install django
```

3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

5. Run Server

```bash
python manage.py runserver
```

---

How It Works

Admin:

* Logs into `/admin`
* Adds events with category (Tech / Cultural / Sports)

Student:

* Logs into system
* Clicks event category
* Views all events dynamically fetched from database

---

Key Concept

> Event categories act as **filters**, and all event data is dynamically fetched from the database instead of being hardcoded.

Future Enhancements

* Event registration system
* Admin approval workflow
* Event images upload
* Search & filter functionality
* User dashboard

Demo Preview

> Add screenshots here (Home Page, Event Page, Admin Panel)

 Contributing

Feel free to fork the project and improve it. Suggestions and improvements are welcome!

License

This project is for educational purposes.

Author

Developed as a college-level project to demonstrate **Django fundamentals, authentication, and dynamic content rendering**.
