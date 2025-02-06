# Django Authentication System

##  Overview
This project is a **Django-based authentication system** that includes essential features like **user registration, login, logout, password reset, and profile management**. The authentication system is built using Django's built-in authentication framework and custom enhancements.

## 🚀 Features
- **User Registration** (Signup with email & username)
- **User Login** (Supports login via username or email)
- **User Logout**
- **Dashboard & Profile Page**
- **Change Password (Authenticated users only)**
- **Forgot Password (Email-based reset link)**
- **Reset Password via email verification**
- **Error handling & validation**

##  Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/milan903575/django-user-authentication.git
cd django-user-authentication/Authentication
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install django

```

### 4️⃣ Configure `settings.py` File (for Email Reset)
Update the  `settings.py` file in the authentication folder and configure email settings:
```

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'milansooraj93@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'ifag urwx cjry fsst'  # Use an App Password if using Gmail
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### 5️⃣ Apply Migrations & Create Superuser
```sh
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```sh
python manage.py runserver
```

##  Usage
1. **Signup:** Users can create an account with a valid email.
2. **Login:** Supports both username and email login.
3. **Dashboard:** A private area for logged-in users.
4. **Profile Page:** Users can view their profile.
5. **Change Password:** Users can update their passwords.
6. **Forgot Password:** Users receive a reset link via email.
7. **Reset Password:** Users can set a new password after email verification.

##  Folder Structure
```
├── user_authentication
│   ├── views.py       # Authentication logic
│   ├── forms.py       # Custom authentication forms
│   ├── urls.py        # Routes for auth pages
│   ├── templates
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   ├── change_password.html
│   │   ├── forgot_password.html
│   │   ├── reset_password.html
│   └── static
│       ├── style.css  # Styling for auth pages
```

##  API Endpoints
| URL Pattern             | View Function         | Description |
|-------------------------|----------------------|-------------|
| `/signup/`             | `signup_view()`       | User Registration |
| `/login/`              | `login_view()`        | User Login |
| `/logout/`             | `logout_view()`       | User Logout |
| `/dashboard/`          | `dashboard_view()`    | User Dashboard |
| `/profile/`            | `profile_view()`      | View Profile |
| `/change-password/`    | `change_password_view()` | Change Password |
| `/forgot-password/`    | `forgot_password_view()` | Forgot Password |
| `/reset-password/<uid>/<token>/` | `reset_password_view()` | Reset Password |


