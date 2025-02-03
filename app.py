from flask import Flask, render_template, abort, request, jsonify, send_file, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object('config.Config')

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
cache = Cache(app)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)

# Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def index():
    # Render the index page
    return render_template("index.html")

@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann",
        "'BUY GOLD'",
        "'pipis 2'",
        "'no kromer' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "HaLLO!!!!!!!"
    ]
    # Select a random quote
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    # Render the test page with the selected quote
    return render_template('test.html', name=name, quote=quote, style=True)

@app.route("/members")
def members():
    try:
        members_list = [
            {"name": "xuya", "role": "Admin"},
            {"name": "peppy", "role": "dios"},
            {"name": "simon", "role": "Moderator"}
        ]
        return render_template('members.html', members=members_list)
    except Exception as e:
        app.logger.error(f'Error in members route: {str(e)}')
        return render_template('500.html'), 500

@app.route("/members/<string:name>/")
def getMember(name):
    try:
        members_list = [
            {"name": "xuya", "role": "Admin"},
            {"name": "peppy", "role": "dios"},
            {"name": "simon", "role": "Moderator"}
        ]
        
        # Find the member by name (case-insensitive)
        member = next((m for m in members_list if m['name'].lower() == name.lower()), None)
        
        if member:
            return render_template('member.html', member=member)
        else:
            return render_template('404.html'), 404
    except Exception as e:
        app.logger.error(f'Error in getMember route: {str(e)}')
        return render_template('500.html'), 500

@app.route("/api/members", methods=['GET'])
def api_members():
    try:
        members_list = [
            {"name": "xuya", "role": "Admin"},
            {"name": "peppy", "role": "dios"},
            {"name": "simon", "role": "Moderator"}
        ]
        return jsonify(members_list)
    except Exception as e:
        app.logger.error(f'Error in api_members route: {str(e)}')
        return jsonify({"error": "Internal server error"}), 500

@app.route("/upload", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully'}), 200

@app.route("/stats")
def get_stats():
    members_list = [
        {"name": "xuya", "role": "Admin"},
        {"name": "peppy", "role": "dios"},
        {"name": "simon", "role": "Moderator"}
    ]
    stats = {
        'total_members': len(members_list),
        'server_time': datetime.now().isoformat(),
        'version': '1.0.0'
    }
    return jsonify(stats)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            flash('Logged in successfully.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route("/posts", methods=['GET', 'POST'])
@login_required
@limiter.limit("100/day")
@cache.cached(timeout=300)
def posts():
    if request.method == 'POST':
        post = Post(
            title=request.form['title'],
            content=request.form['content'],
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        cache.delete('posts')
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts.html', posts=posts)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
