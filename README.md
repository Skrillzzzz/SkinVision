# 🧠 SkinVision – Skin Cancer Annotation Tool

SkinVision is a web-based tool designed to assist medical professionals and researchers in annotating dermoscopic images for skin cancer diagnosis. Users can upload skin images, draw annotations directly on them, and export the data for machine learning or clinical review.

## 🎓 Dissertation Context

This project was built as part of my final-year dissertation for a BSc in Software Engineering at Manchester Metropolitan University. It aims to support medical professionals by providing a simple, accessible interface for labelling skin cancer features in medical imagery.
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
```text
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
```


## 🧪 How to Run Locally

# 1. Clone the repository
git clone https://github.com/Skrillzzzz/SkinVision.git
cd SkinVision

# 2. Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver

# 6. Access the app
Visit http://127.0.0.1:8000 in your browser.

## 📸 Screenshots

![Annotation Interface](screenshots/annotation-ui.png)

## 🧪 Future Improvements

Support for multiple annotation shapes (polygon, brush)
Advanced filtering and image tagging
Integration with machine learning models for predictive analysis
Docker support for easier deployment

## 🙋‍♂️ Author

Andrew Melving
Software Engineering Graduate | Cybersecurity & Full-Stack Enthusiast
[LinkedIn](https://www.linkedin.com/in/andrew-melving-138483209/) | [GitHub](https://github.com/Skrillzzzz/SkinVision/edit/main/README.md)
