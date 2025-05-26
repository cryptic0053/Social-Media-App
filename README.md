# 🌐 Social Media App (Django)

A feature-rich social media platform built using **Django**, enabling users to register, share posts, follow others, and interact with content. Hosted on Render.

🔗 **Live Demo:** [Visit the App](https://social-media-app-3-1889.onrender.com/loginn/?next=/)

---

## 📌 Features

### 👤 User Management
- User registration and login
- Profile creation and updates
- Secure authentication system

### 📝 Posts & Media
- Create, edit, and delete posts
- Upload and display images with posts
- Display feed from followed users

### 🔍 Explore & Social Features
- Follow/unfollow other users
- Search users by name
- View global feed and explore profiles

---

## 🛠️ Technologies Used

- **Backend:** Django 5.1.4
- **Database:** SQLite (for development)
- **Frontend:** HTML, CSS, Bootstrap
- **Deployment:** Render
- **Python Version:** 3.11
- **WSGI Server:** Gunicorn

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/cryptic0053/Social-Media-App.git
cd Social-Media-App
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📸 ER Diagram

![ER Diagram](https://github.com/cryptic0053/Social-Media-App/blob/main/ER-diagram.png)

---

## 🧪 Test Credentials

| Role       | Username | Password |
|------------|----------|----------|
| Admin      | admin    | admin123 |
| Test User  | testuser | test123  |

---

## ⚠️ Deployment Tips (Render)

- Ensure your `gunicorn` command uses:
  ```
  gunicorn socialmedia_app.wsgi:application
  ```
- Add your Render domain to `ALLOWED_HOSTS` in `settings.py`
- Set `DEBUG = False` for production

---

## 👤 Author

Developed by [@cryptic0053](https://github.com/cryptic0053)

Contributions and feedback are welcome!
