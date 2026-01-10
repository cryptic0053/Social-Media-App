# 🌐 Social Media App

![Django](https://img.shields.io/badge/Django-5.0%2B-green) ![Python](https://img.shields.io/badge/Python-3.11%2B-blue) ![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple) ![Status](https://img.shields.io/badge/Deployed-Render-success)

A feature-rich social media platform designed to connect people. Built with **Django**, this application allows users to share life updates, follow friends, and explore global content in a secure, responsive environment.

🚀 **Live Demo:** [https://social-media-app-tau-nine.vercel.app](https://social-media-app-tau-nine.vercel.app) *(or your specific Render link)*

---

## 📌 Key Features

* **🔐 Authentication:** Secure Sign Up, Login, and Logout functionality.
* **👤 User Profiles:** Customizable profiles with bio, profile pictures, and post history.
* **📝 Social Feed:**
    * **Global Stream:** View posts from all users.
    * **Personalized Feed:** See content only from people you follow.
* **🤝 Network System:** Follow and Unfollow users to curate your feed.
* **🖼️ Media Support:** Upload and display high-quality images with posts.
* **🔎 Discovery:** Search functionality to find users by username.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Django 5.1 (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 4 |
| **Database** | SQLite (Dev) / PostgreSQL (Prod) |
| **Storage** | Django Media / Cloudinary (Optional) |
| **Deployment** | Render / Vercel |

---

## 📂 Project Structure

```bash
.
├── socialmedia/          # Project Settings (WSGI, ASGI, URLs)
├── userauth/             # Authentication & Profile Logic
├── templates/            # HTML Templates (Bootstrap UI)
├── static/               # CSS, JS, Images
├── media/                # User Uploaded Content
├── manage.py             # Django CLI
├── db.sqlite3            # Database
└── requirements.txt      # Dependencies

```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/cryptic0053/Social-Media-App.git](https://github.com/cryptic0053/Social-Media-App.git)
cd Social-Media-App

```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Apply Migrations

Initialize the database schema for users and posts.

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Create Superuser (Optional)

To manage users and posts via the admin panel:

```bash
python manage.py createsuperuser

```

### 6. Run Server

```bash
python manage.py runserver

```

*Access the app at `http://127.0.0.1:8000/*`

---

## 📸 Database Schema

*(See `ER-diagram.png` in the repo for the full Entity-Relationship visualization)*

The database manages complex relationships including:

* **Users** (Custom AbstractUser)
* **Profiles** (One-to-One with User)
* **Posts** (ForeignKey to User)
* **Followers** (Many-to-Many Relationship)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch and open a Pull Request.

---

## 👤 Author


* GitHub: [@cryptic0053](https://github.com/cryptic0053)

---

* This project is for educational purposes.
