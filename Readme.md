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
Your app should now be running at `http://127.0.0.1:8000/admin`

## 💐 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/admin`      | POST   | Admin Panel |
| `/api/faqs/`  | GET    | Fetch all FAQs in all languages |
| `/api/faqs/?lang=hi` | GET    | Fetch the FAQs in Hindi only |
| `/api/faqs/?lang=en` | GET   | Fetch the FAQs in English only |

### 📚 API Response Example
When accessing `http://16.171.132.17:8000/api/faqs/`, the response is as follows:
```json
{
  "faqs": [
    {
      "question_en": "What is Django?",
      "answer_en": "Django is a Python-based web framework.",
      "question_hi": "Django क्या है?",
      "answer_hi": "Django एक Python-आधारित वेब फ्रेमवर्क है।"
    }
  ]
}
```

When fetching only Hindi FAQs using `http://16.171.132.17:8000/api/faqs/?lang=hi`, the response is:
```json
{
  "faqs": [
    {
      "question_hi": "Django क्या है?",
      "answer_hi": "Django एक Python-आधारित वेब फ्रेमवर्क है।"
    }
  ]
}
```

## 📚 Technologies Used
- **Django** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **AWS EC2 instance** - For deploying the server  

## 🌐 Backend Hosting
The backend of this application is hosted on AWS EC2 and can be accessed at:
🔗 Admin Panel: http://16.171.132.17:8000/admin

🆔 Username: praveen
🔑 Password: satyam123

## 📝 Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## 🤖 Testing with `pytest`

### Install `pytest` for testing and coverage
```bash
pip install pytest pytest-cov
```

### Run Tests with Coverage Report
```bash
pytest --cov=your_project_name --cov-report=html
```

## 🛡 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any queries or suggestions, feel free to reach out to:
📧 Email: satyammaurya9620@gmail.com  
📱 Phone: +91 8302252848  
🔗 GitHub: [satyam-svg](https://github.com/satyam-svg)

