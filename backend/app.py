from flask import Flask
from models import db
from config import Config
from flask_login import LoginManager
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# to create all database tables
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return 'Hello, World!'


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'  # Specify the login view
login_manager.init_app(app)

# User loader function
@login_manager.user_loader
def load_user(user_id):
    from models import User  # Import inside the function to avoid circular imports
    #find the user by username instead of converting to int
    return User.query.filter_by(username=user_id).first()


# Define some hardcoded users (for testing purposes)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = None  # Add a user ID attribute
        
    def is_authenticated(self):
        return True  # Assuming all users are authenticated

    def is_active(self):
        return True  # Assuming all users are active

    def is_anonymous(self):
        return False  # Assuming no anonymous users

    def get_id(self):
        return str(self.id)  # Return the user ID as a string

# Hardcoded users (for testing)
users = [
    User('user1', 'password1'),
    User('user2', 'password2'),
    User('user3', 'password3')
]

# Assign user IDs
for i, user in enumerate(users, start=1):
    user.id = i

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password match any hardcoded user
        for user in users:
            if user.username == username and user.password == password:
                # Simulate logging in the user
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
        
        flash('Invalid username or password', 'danger')

    return render_template('login.html')


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Get form data from request
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if password matches confirm_password
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))

        # Check if username or email already exists in the database
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))

        # Create new user instance
        new_user = User(username=username, email=email, password=password)

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Image Upload route
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        # Handle image upload logic
        pass  # Placeholder for now
    return render_template('upload.html')

# Annotation Interface route
@app.route('/annotate')
@login_required
def annotate():
    return render_template('annotate.html')

# User Profile route
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
