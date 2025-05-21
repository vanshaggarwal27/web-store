# 🛍️ Web Store

A simple web-based store application built with Flask, designed to manage user interactions and display products. This project serves as a foundational template for developing e-commerce platforms.

---

## 📁 Project Structure

```
web-store/
├── app.py
├── requirements.txt
├── users.db
├── templates/
│   └── *.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── assets/
└── SRS.docx
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.11+
- `pip` (Python package installer)

### ⚙️ Installation Steps

```bash
# Clone the repository
git clone https://github.com/vanshaggarwal27/web-store.git
cd web-store

# Create and activate a virtual environment
python3.11 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

Then open your browser and visit: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment Guide

### 📦 Deploying Locally with Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Run the app using gunicorn
gunicorn app:app
```

To make sure it's deployed correctly, visit your server IP or domain at port 8000 (default).

---

### 🚀 Deploying to Render

1. Add a `render.yaml` file to your project root:

```yaml
services:
  - type: web
    name: web-store
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
```

## Deployment

This project is deployed at: [https://genxia.xyz](https://genxia.xyz)

