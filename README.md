# 📝 BlogHub - Django Blog Website

A full-featured Blog Website built using Django.

This project allows users to register, login, create posts, edit and delete their own posts, comment on posts, and like/unlike posts.  
The project also includes an Admin Panel to manage users, posts, comments, and likes.

---

## 🚀 Features

### ✅ User Authentication
- User Registration (Full Name, Email, Password)
- Email-based Login
- Secure Logout
- Only authenticated users can create, edit, or delete posts

### ✅ Blog Post Management
- Create new blog posts
- Edit own posts
- Delete own posts
- Each post includes:
    - Title
    - Content
    - Author
    - Created Date
    - Optional Image

### ✅ Comment System
- Authenticated users can add comments
- Comments displayed under each post
- Comment author profile image shown

### ✅ Like System
- Users can Like / Unlike posts
- Each post displays total number of likes

### ✅ Profile System
- User Profile with:
    - Profile Image
    - Full Name
    - Email
    - Bio
    - Total Posts
- Edit Profile option

### ✅ Admin Panel
- Manage Users
- Manage Posts
- Manage Comments
- Manage Likes
- Admin and Superuser only visible in Admin user list
- Admin login redirected to `/admin`

---

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Django Admin Panel

---

## 📂 Project Structure
blog_project/
│
├── blog/
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ ├── urls.py
│
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt

---


## ⚙️ Installation Guide

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/utsho261/bloghub.git
```
### 2️⃣ Navigate into the project folder
```bash
cd bloghub
```
### 3️⃣ Create a virtual environment
```bash
python -m venv venv
```
Activate it:
**Windows:**
```bash
venv\Scripts\activate
```
**Mac/Linux:**
```bash
source venv/bin/activate
```
### 4️⃣ Install dependencies
```bash
pip install django
pip install pillow
```
### 5️⃣ Run migrations
```bash
python manage.py migrate
```
### 6️⃣ Create Superuser
```bash
python manage.py createsuperuser
```
### 7️⃣ Run the development server
```bash
python manage.py runserver
```
Open your browser and go to:

```
http://127.0.0.1:8000/
```


🔐 Admin Access
Admin panel:
```
http://127.0.0.1:8000/admin/
```
Only staff or superuser accounts can access admin panel.