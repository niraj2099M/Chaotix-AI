# Project Overview
This Django project leverages Celery for parallel image generation using the Stability AI Text-to-Image API.

## Key Features:
- Django REST Framework API for handling image generation requests and providing browsable API interfaces.
- Celery for asynchronous task management and parallel processing.
- Redis as the Celery broker.
- Integration with Stability AI's Text-to-Image API.
- Basic image metadata storage.


## Requirements
- Python 3.x
- Django
- Django REST Framework
- Redis
- Celery
- Stability AI API Key

## Setup Instructions

### 1. Clone the Repository
```bash
gh repo clone niraj2099M/Chaotix-AI
cd Chaotix-AI/

```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Redis Installation
Ensure that Redis is installed and running on your machine. 

**On Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis-server
```

### 4. Set environment variables: Add a .env file and add the following
- STABILITY_API_KEY: Your Stability AI API key
- STABILITY_API_URL: Your Stability API URL

### 5. Django Setup
Migrate the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Application

### 1. Start the Celery worker:
```bash
celery -A chaotixAI worker -l info
```

### 2. Start the Django development server:
```bash
python3 manage.py runserver
```

## API Endpoints
- open browser and go to http://127.0.0.1:8000/
- send a POST request body
```
    {
      "prompts": ["image1 description", "image2 description", "image3 description"]
    }
