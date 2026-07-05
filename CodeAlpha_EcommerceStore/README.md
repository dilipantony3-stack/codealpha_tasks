# 🛍️ ShopEase — Django E-Commerce Store

A full-featured e-commerce web application built with **Django (Python)** backend and **HTML/CSS/JavaScript** frontend.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🛒 Shopping Cart | Session-based (guests) + user-linked carts with auto-merge on login |
| 📦 Product Catalogue | Categories, search, filtering, stock management |
| 🔍 Product Detail | Full info, related products, quantity selector |
| 📋 Order Processing | Checkout → order confirmation → order history with status tracking |
| 👤 User Auth | Register, login, logout, profile with shipping address |
| 🗄️ SQLite Database | Products, Users, Profiles, Carts, Orders — all stored |
| 🛠️ Admin Panel | Full Django admin at `/admin/` |

---

## 🚀 Quick Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run database migrations

```bash
python manage.py migrate
```

### 3. Seed sample data (products + admin account)

```bash
python seed_data.py
```

This creates:
- **12 sample products** across 5 categories
- **Admin account**: `admin` / `admin123`

### 4. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## 📂 Project Structure

```
ecommerce_project/
├── ecommerce/               # Django project settings
│   ├── settings.py
│   └── urls.py
├── store/                   # Main app
│   ├── models.py            # Database models
│   ├── views.py             # All view logic
│   ├── forms.py             # Registration, profile, checkout forms
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin configuration
│   └── context_processors.py
├── templates/
│   ├── store/               # HTML templates
│   └── registration/        # Auth templates
├── static/
│   ├── css/style.css        # Complete design system
│   └── js/main.js
├── media/                   # Uploaded product images
├── seed_data.py             # Sample data loader
├── requirements.txt
└── manage.py
```

---

## 🔑 Admin Panel

Visit **http://127.0.0.1:8000/admin/** and log in with `admin` / `admin123`.

From admin you can:
- Add/edit/delete products and categories
- Upload product images
- View and update order statuses
- Manage users

---

## 📸 Adding Product Images

1. Go to `/admin/` → Products → select a product
2. Upload an image in the Image field
3. Images are stored in `media/products/`

---

## 🗺️ URL Map

| URL | Page |
|---|---|
| `/` | Home / featured products |
| `/products/` | Product listing with filters |
| `/products/<slug>/` | Product detail |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout (login required) |
| `/orders/` | Order history (login required) |
| `/orders/<id>/` | Order detail |
| `/register/` | User registration |
| `/login/` | Login |
| `/profile/` | User profile |
| `/admin/` | Django admin |

---

## 🛠️ Customisation

- **Add payment gateway**: Integrate Stripe or Razorpay in `views.py → checkout()`
- **Email notifications**: Configure `EMAIL_*` settings and send on order creation
- **More categories**: Add via admin panel or `seed_data.py`
- **Production**: Set `DEBUG=False`, use PostgreSQL, configure `ALLOWED_HOSTS`
