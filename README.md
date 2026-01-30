# HRMS Lite – Human Resource Management System

HRMS Lite is a lightweight Human Resource Management System built using **Django** with **JavaScript-enhanced UI**.  
It allows organizations to manage employees and record daily attendance with a clean, responsive, and user-friendly interface.

The project focuses on simplicity, usability, and core HR functionality without over-engineering.

---

## 🚀 Features

- Add and manage employees
- View employee records
- Mark daily attendance
- View attendance history
- JavaScript-enhanced form interactions
- Clean light-theme backend UI
- Django Admin support
- Proper HTTP status handling
- Success and error notifications

---

## 🛠 Tech Stack

### Backend
- Python
- Django

### Frontend
- Django Templates
- Tailwind CSS
- JavaScript (form behavior, UI enhancements)

### Database
- SQLite (default)
- Can be extended to PostgreSQL or MySQL

---

## 📁 Project Structure

hrms_lite/
├── hrms/ # Project settings
├── hrms_app/ # Core application
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── templates/
│ └── static/
│ └── js/
│ └── main.js
├── db.sqlite3
├── manage.py
└── README.md


---

## 🖥️ Run the Project Locally

Follow the steps below to run the HRMS Lite project on your local machine.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hrms_lite.git
cd hrms_lite
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py runserver


## 🔐 Admin Access

Use the following credentials to access the Django Admin panel:

**Admin URL**  
http://127.0.0.1:8000/admin/
Username - admin
Password - admin@123

**for server**
https://hrms-lite-5du2.onrender.com/
Username - admin
Password - admin@123