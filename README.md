# 🧠 SkinVision – Skin Cancer Annotation Tool

SkinVision is a web-based tool designed to assist medical professionals and researchers in annotating dermoscopic images for skin cancer diagnosis. Users can upload skin images, draw annotations directly on them, and export the data for machine learning or clinical review.

## 🚀 Features

🖼️ Upload dermoscopic images for analysis
✍️ Annotate and label key skin features
💾 Save annotation data in a structured SQL database
📤 Export data for medical or academic use
🔐 Basic user authentication


## 🛠️ Tech Stack

Backend: Python, Django
Frontend: HTML, CSS, JavaScript
Database: SQLite (dev) | PostgreSQL (prod-ready)
Tools: Django Admin, Pillow, Git/GitHub

## 📁 File Structure
skinvision/
├── annotations/          # App for handling image and annotation logic
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── users/                # Handles user registration and login
│   ├── models.py
│   └── views.py
│
├── templates/            # HTML templates
├── static/               # Static JS and CSS files
├── media/                # Uploaded images
├── db.sqlite3            # Database file (for local use)
├── manage.py
└── requirements.txt

## 🧪 How to Run Locally

# 1. Clone the repository
git clone https://github.com/Skrillzzzz/SkinVision.git
cd SkinVision

# 2. Set up a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver

# 6. Visit http://127.0.0.1:8000 in your browser.

## 📸 Screenshots

(You can add images to a /screenshots folder and embed them here like this:)
![Annotation Interface](screenshots/annotation-ui.png)

## 🎓 Dissertation Context

This project was built as part of my final-year dissertation for a BSc in Software Engineering at Manchester Metropolitan University. It aims to support medical professionals by providing a simple, accessible interface for labelling skin cancer features in medical imagery.
