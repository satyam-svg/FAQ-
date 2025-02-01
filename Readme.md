

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

## 📡 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/admin`      | POST   | Admin Panel |
| `/api/faqs/`  | GET    | Fetch all FAQs in all languages |
| `/api/faqs/?lang=hi` | GET    | Fetch the FAQs with language=Hindi |
| `/api/faqs/?lang=en` | GET   | Fetch the FAQs with language=English |

## 📚 Technologies Used
- **Django** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Docker** (Optional) - Containerization
- **Celery & Redis** (Optional) - Asynchronous task management
- **AWS EC2 instance** - For deploying the server  

## 🌐 Backend Hosting
The backend of this application is hosted on AWS EC2 and can be accessed at:
[http://16.171.132.17:8000/admin](http://16.171.132.17:8000/admin)

-username: praveen
-password: satyam123

## 📖 AWS Deployment Documentation
For deploying Django on AWS EC2, follow these steps:

1. **Launch an EC2 Instance**
   - Go to AWS EC2 Dashboard and launch an Ubuntu instance.
   - Configure security groups to allow HTTP, HTTPS, and SSH access.

2. **Connect to the Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-instance-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip python3-venv nginx -y
   ```

4. **Clone the Project & Set Up Virtual Environment**
   ```bash
   git clone https://github.com/satyam-svg/FAQ-.git
   cd FAQ-
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Run Migrations & Start Server**
   ```bash
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8000
   ```

6. **Set Up Gunicorn & Nginx for Production**
   ```bash
   pip install gunicorn
   gunicorn --bind 0.0.0.0:8000 your_project.wsgi:application
   ```

7. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/django
   ```
   Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name your-ec2-instance-ip;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   ```
   Enable the configuration:
   ```bash
   sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

Now, your Django FAQ app is live on AWS EC2.

## 📝 Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request



## 🧪 Testing and Coverage Report with `pytest`

### Install `pytest` and `pytest-cov` for testing and coverage

You can use `pytest` to test your Django application, along with `pytest-cov` to measure code coverage. Here's how to integrate it into your project.

#### 1️⃣ Install `pytest` and `pytest-cov`

```bash
pip install pytest pytest-cov
```

#### 2️⃣ Create a Test File (e.g., `test_faqs.py`)

You can create a test file that will test your API endpoints. Here's an example:

```python
import pytest
import requests

@pytest.mark.django_db
def test_faqs_api():
    # URL of your API endpoint
    url = "http://127.0.0.1:8000/api/faqs/"
    
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert 'faqs' in data
    assert isinstance(data['faqs'], list)
    assert len(data['faqs']) > 0
```

#### 3️⃣ Run Tests with Coverage Report

To run tests and get a coverage report, execute the following command:

```bash
pytest --cov=your_project_name --cov-report=html
```

This will run the tests and generate a coverage report in HTML format.

#### 4️⃣ View the Coverage Report

After running the tests, an `htmlcov` folder will be generated. Open the `index.html` file in a web browser to view the detailed coverage report.

---

### **Image Support in Documentation**

If you want to include images in your documentation (e.g., screenshots or diagrams), you can place images in a directory like `docs/images` and refer to them in your README like this:

```markdown
![Diagram](/coverage.png)
```

This will display the image `coverage_report.png` located in the `docs/images` folder.

---

## 🛡 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any queries or suggestions, feel free to reach out to:
📧 Email: satyammaurya9620@gmail.com  
📱 Phone: +91 8302252848  
🔗 GitHub: [satyam-svg](https://github.com/satyam-svg)

---
