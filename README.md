# Ultrahyperbasic Flask WebApp

Welcome to my Ultrahyperbasic Python WebApp! This project (easily freaking longest think i have EVER made) is a simple web application built using Flask, designed to demonstrate the basics of web development with Python. It includes user authentication, member management, and a simple post creation feature. (GOD I HATED DOING THAT)

## Features

- User Registration and Login
- Member Management
- Post Creation and Display
- File Uploads
- API Endpoints for Members
- Rate Limiting and Caching
- Error Handling Pages (404 and 500) (Had to include em, i almost punched my PC to death)

# WARNING
# BEGGINER PROJECT. I'LL BE LEAVING THE REQUIREMENTS, DON'T SCOLD ME (too hard) FOR THE LIKELY MANY MISTAKES I MADE

## Requirements

Requirements
Python 3+
Flask 2.3.3
Flask-SQLAlchemy 3.1.1
Flask-Login 0.6.2
Flask-Migrate 4.0.4
Flask-WTF 1.1.1
email-validator 2.0.0
python-dotenv 1.0.0
gunicorn 20.1.0
pytest 6.2.5
flask-cors 3.0.10
flask-restful 0.3.9
flask-jwt-extended 4.3.1
requests 2.26.0
pillow 8.3.2
Flask-Limiter 3.5.0
Flask-Caching 2.0.2
bcrypt 4.0.1
marshmallow 3.19.0
Werkzeug 2.3.7

## Installation

Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/ultrahyperbasic-flask-webapp.git
    cd ultrahyperbasic-flask-webapp
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**
    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development
    export SECRET_KEY=your-super-secret-key
    export DATABASE_URL=sqlite:///app.db
    ```

5. **Start the database:**
    ```sh
    flask db upgrade
    ```

6. **Run the application:**
    ```sh
    flask run
    ```

## Usage
## Usage

- **Home Page:** Access the home page at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- **Register:** Create a new account at [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register).
- **Login:** Log in to your account at [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login).
- **Members:** View the list of members at [http://127.0.0.1:5000/members](http://127.0.0.1:5000/members).
- **Posts:** Create and view posts at [http://127.0.0.1:5000/posts](http://127.0.0.1:5000/posts).

## API Endpoints

- **Get Members:** `GET /api/members` - Retrieve a list of members.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change and allat. This is dogwater, but still took me alot.

## License

This project is licensed under the MIT License. See the [LICENSE](Ultrahyperbasic-Flask-WebApp-/LICENSE/LICENSE) file for details.

## Contact

For any questions or suggestions, please contact:

- Instagram: polterwine_egoz>

---

Thank you for checking out the Ultrahyperbasic Flask WebApp! 
this sucks
