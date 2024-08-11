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
git clone https://github.com/Mohit-majumdar/Chaotix-text-to-image-assessment/.git
cd Chaotix-text-to-image-assessment/
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
- STABILITY_API_URL: 
