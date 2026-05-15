# OnlineShop

## Overview
OnlineShop is a full-featured e-commerce backend built with Django and Django REST Framework. It provides APIs for user management, product catalog, shopping cart, order processing, and payment handling. The project is modular, scalable, and ready for integration with frontend clients or mobile apps.

## Features
- User registration, authentication, and roles (Admin, Seller, User)
- Product categories and product management
- Shopping cart with cart items
- Order creation and status tracking
- Multiple payment methods and payment status management
- JWT-based authentication
- Filtering and pagination for product listings
- CORS support for frontend integration

## Tech Stack
- Python 3
- Django 6
- Django REST Framework
- SimpleJWT (JWT authentication)
- SQLite (default, can be swapped for PostgreSQL/MySQL)
- Pillow (image support)
- django-cors-headers

## Project Structure
```
├── cart/        # Shopping cart app
├── config/      # Django project settings and URLs
├── order/       # Order management app
├── payment/     # Payment processing app
├── product/     # Product and category management
├── user/        # Custom user model and authentication
├── templates/   # HTML templates (index.html)
├── db.sqlite3   # SQLite database (default)
├── manage.py    # Django management script
├── requirements.txt
```

## Installation & Setup
1. **Clone the repository:**
	```bash
	git clone <repo-url>
	cd onlineshop
	```
2. **Create and activate a virtual environment:**
	```bash
	python -m venv venv
	source venv/Scripts/activate  # On Windows
	# or
	source venv/bin/activate      # On macOS/Linux
	```
3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
4. **Configure environment variables:**
	- Create a `.env` file in the root directory with the following variables:
	  ```env
	  SECRET_KEY=your_secret_key
	  DEBUG=True
	  ALLOWED_HOSTS=127.0.0.1,localhost
	  ```
5. **Apply migrations:**
	```bash
	python manage.py migrate
	```
6. **Create a superuser (admin):**
	```bash
	python manage.py createsuperuser
	```
7. **Run the development server:**
	```bash
	python manage.py runserver
	```

## API Endpoints
- All API endpoints are prefixed with `/api/`.
- Example endpoints:
  - `POST /api/user/register/` – Register a new user
  - `POST /api/user/login/` – Obtain JWT token
  - `GET /api/product/` – List products
  - `POST /api/cart/` – Add item to cart
  - `POST /api/order/` – Create order
  - `POST /api/payment/` – Make payment

## Running Tests
```bash
python manage.py test
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please open an issue in the repository.