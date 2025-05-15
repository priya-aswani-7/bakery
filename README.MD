# 🧁 The Bakery – A Django CRUD Learning Project

Welcome to **The Bakery**, a simple Django web app built to help beginners learn how to implement basic CRUD (Create, Read, Update, Delete) functionality. This project focuses on managing cakes, customers, and orders in a fictional bakery.

---

## 🚀 Project Overview

This project teaches the core of Django web development by building a minimal bakery management system with:

- ✅ Cake management (add, view, update, delete)
- 👤 Customer management (add, view, update, delete)
- 📦 Order creation and tracking

---

## 🧱 Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** Django Templates
- **Admin Panel:** Django Admin (auto-generated)

---

## 🔧 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/priya-aswani-7/bakery.git
cd bakery
````

### 2. Create and activate a virtual environment

```bash
pipenv shell
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Start the Django project

```bash
django-admin startproject bakery .
```

### 5. Create the app

```bash
python manage.py startapp main_app
```

### 6. Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app.

---

## 🛠 Features to Build

| Feature      | Model    | Description                              |
| ------------ | -------- | ---------------------------------------- |
| Add cake     | Cake     | Create and save a new cake to the system |
| View cakes   | Cake     | Display a list of all cakes              |
| Edit cake    | Cake     | Update cake details                      |
| Delete cake  | Cake     | Remove a cake from the system            |
| Add customer | Customer | Save new customer info                   |
| Place order  | Order    | Connect customer + cake + quantity       |

---

## 🖼️ Entity Relationship Diagram

("C:\Users\Priya\Downloads\Blank diagram (2).png")


## 📌 Learning Goals

* Build and relate models in Django
* Create views and templates for CRUD
* Use Django Admin and Forms
* Understand project structure and routing

---

## 🧑‍💻 Contributing

This is a student learning project. Contributions and improvements are welcome!

---

## 📄 License

This project is open source and free to use for educational purposes.

---

Happy baking & building! 🍰

