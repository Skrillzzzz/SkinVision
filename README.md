### README Text File for SkinVisionApp

---

Project Name: SkinVisionApp  
Version: 1.0  
Author: Andrew Melving

Description:  
Skin Vision is a web-based application designed for the efficient annotation of skin images. This tool allows users to upload, annotate, and track changes in skin lesions over time, enhancing monitoring and diagnostic processes in dermatological practices.

---

System Requirements:
- Operating System: Windows 10 or higher, MacOS 10.12 or higher, Linux
- Web Browser: Latest version of Google Chrome, Mozilla Firefox, or Safari

Software Requirements:
- Python: Version 3.8 or higher
- Django: Version 3.2 or higher
- Database: SQLite3 (included with Django)

---

Installation Instructions:

1. Clone the Repository:
   - Clone this repository to your local machine using `git clone [repository URL]`.

2. Set Up a Virtual Environment:
   - Navigate to the project directory and run `python -m venv venv` to create a virtual environment.
   - Activate the environment:
     - Windows: `.\venv\Scripts\activate`
     - MacOS/Linux: `source venv/bin/activate`
	
	Python Interpreter: /backend/venv/bin/python

3. Database Setup:
        - Django uses SQLite3 by default, so no additional database setup is needed
		for development purposes.
	- Apply database migrations by running python manage.py migrate.

4. Run the Application:
   - Start the server with `python manage.py runserver`.
   - Access the app via `localhost:8000` in your web browser.

---

Usage Instructions:
- Login/Register: Begin by registering a new user or logging in with existing credentials.
- Upload Images: Navigate to the 'Upload Images' section to upload new skin images.
- Annotating Images:
	Upload an image of the area of concern
	Use the annotation tools available in the 'Annotation Tool' section to mark 		and note areas on uploaded images.
	Click on save annotation button, annotated image is uploaded to the users 		local files
	Go to Upload Image page and upload annotated Image
- View Annotations: Access and review saved annotations in the 'User Profile' section under 'Image Gallery'.

Troubleshooting Common Issues:
- Database Connection Errors: Ensure SQLite credentials in `settings.py` match your SQLite setup.

---

Additional Materials Included:
- Presentation Slides
- Images for each page

For any further assistance, please contact tunmise30@gmail.com

