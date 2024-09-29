# Coffee Webstore

Welcome to the **Coffee Webstore**, a private project designed to showcase a range of coffee products and related items in an intuitive and user-friendly web interface.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

## Features
- Browse and filter coffee products.
- Add products to a shopping cart.
- View product details with images and descriptions.
- Categories for easy navigation.
- User authentication with sign-in functionality.
- Make purchasing (both online payment and COD)

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Database**: SQLite (development), MySQL/PostgreSQL (production)
- **Version Control**: Git
- **Hosting**: Docker

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/coffee-webstore.git
   cd coffee-webstore
   python manage.py runserver
   ```

2. Directories structure
coffee-webstore/
│
├── store/                   # Core app handling products, categories
│   ├── migrations/           # Django migrations
│   ├── templates/            # HTML templates
│   ├── models.py             # Database models
│   └── views.py              # View logic
│
├── static/                   # Static files (CSS, JS, images)
├── templates/                # Base templates
├── manage.py                 # Django management script
├── README.md                 # Project readme
└── requirements.txt          # Python dependencies
