# 🛒 Django E-commerce Project

Welcome to a full-featured E-commerce web application built with **Django**. This platform supports customer shopping experience with product listings, a cart system, and a secure checkout workflow.

![Banner](screenshots/banner.png)

---

## 🚀 Features

- 🧑‍💻 User Registration & Login
- 🛍️ Product Listing with Categories
- 🛒 Shopping Cart System
- 💳 Order Placement & Checkout
- 📦 Admin Dashboard to Manage Products & Orders
- 📱 Responsive UI Design

---

## 🛠️ Built With

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default), PostgreSQL (optional)
- **Authentication:** Django built-in auth
- **UI Framework:** Bootstrap / Tailwind CSS

---

## 📸 Screenshots

> 📁 Make sure to upload your screenshots to a folder called `/screenshots` in your repo.

### 🔹 Homepage

![Homepage](screenshots/homepage.png)

---

### 🔹 Product Listing

![Products](screenshots/products.png)

---

### 🔹 Cart Page

![Cart](screenshots/cart.png)

---

### 🔹 Checkout Page

![Checkout](screenshots/checkout.png)

---

## 🧪 Setup Instructions

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/swajan21/DJANGO-PROJECT-ECOMMERCE.git
cd DJANGO-PROJECT-ECOMMERCE

# 2. Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3. Install the required packages
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
