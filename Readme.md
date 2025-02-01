# Django App README

## 📌 Project Overview
This Django-based web application is designed for managing FAQs with multilingual support. Users can insert questions and answers, making it easy to organize and retrieve frequently asked information. The project leverages Django and Django REST Framework (DRF) to provide a smooth and efficient experience.

## 🚀 Features
- CRUD operations for [FAQ Model]
- API endpoints for interacting with frontend or third-party services
- Integration with databases (SQLite)

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/satyam-svg/FAQ-.git
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5️⃣ Run the Server
```bash
python manage.py runserver
```
Your app should now be running at `http://127.0.0.1:8000/`

## 📡 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/admin`      | POST   | Admin Panell |
| `/api/faqs/`  | GET    | Fetch all faqs in all language |
| `/api/faqs/?lang=hi` | GET    | Fetch the faqs with language=hindi |
| `/api/faqs/?lang=en` | GET   | Fetch the faqs with language=bengali |

## 📚 Technologies Used
- **Django** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Docker** (Optional) - Containerization
- **Celery & Redis** (Optional) - Asynchronous task management
- **AWS EC2 instance**-For deploying the server     

## 📝 Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## 🛡 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any queries or suggestions, feel free to reach out to:
📧 Email: satyammaurya9620@gmail.com 
📱 Phone: +91 8302252848
🔗 GitHub: [satyam-svg](https://github.com/satyam-svg)

