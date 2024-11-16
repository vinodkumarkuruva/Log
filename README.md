
## Title 
 
Referral System API

## Description

A simple REST API built with Flask for user registration, login, and referral tracking.
## Features
- User Registration : Register users with unique referral codes. Optionally register using a valid referral code.

- User Login : Authenticate users using email and password.

- Referral Details : Retrieve user details along with their referred users.

- Extra APIs : Fetch all users with their referral codes.
## Technologies

- Backend: Flask, Flask-SQLAlchemy, Flask-Migrate
- Database: SQLite (or replace with PostgreSQL/MySQL if desired)
-->Installation and Setup

1. Clone the repository :-
 - git clone https://github.com/vinodkumarkuruva/Log.git 
 - cd Log

2. Prerequisites :-
Python 3.7+: Ensure that Python is installed on your system Flask - As a Framework Docker: For containerizing the application

3. Steps to Set Up :-


* Create a virtual environment : python3 -m venv < name of virtual Environment >

* To activate the virtual Environment : < name of virtual Environment >/Scripts/activate

* Install dependencies : pip install -r requirements.txt

* Set up the database : flask db init flask db migrate -m "Initial migration" flask db upgrade

* Run the server : Python app.py 

The application will start and be accessible at http://127.0.0.1:5000

4. Running the Application with Docker

* Build the Docker image : docker build -t < name of image > .

* Run the Docker container : docker run -p 5000:5000 < name of Image >

* The application will be available at http://localhost:5000

5. Tables and Fields :-

* Users id : Unique primary key for each user. 
* email : User's email address, must be unique and non-nullable. 
 * name : Full name of the user, required field. 
* mobile : User's mobile number, must be unique and non-nullable.
 * city : The city where the user resides, required field.
 * referral_code : A unique 10-character referral code generated upon registration. 
 * referrer_id : Links to the ID of the user who referred this user, nullable. 
 * password_hash : Securely hashed password for the user. 
 * registered_at : Timestamp of when the user was registered.
  * referees : Relationship to all users referred by this user.


6. Features of the Model :

 * Automatically generates a unique referral code for each user.
 * Tracks referrals using referrer_id and establishes relationships with referred users (referees).

7.Other Info :-

--> Error Handling: The application returns appropriate HTTP 400 status codes for bad requests, such as when a Users is unavailable .

--> Modularity: The application is designed to be modular, with separate services handling business logic, making the codebase easy to maintain and extend.

--> Docker Support: A Dockerfile is included for containerization, making it easy to deploy the application in different environments.


## Documentation

[Python_Documentation](https://docs.python.org/3/)

[Flask_Documentation](https://flask.palletsprojects.com/en/stable/)

[SQLite_Documentation](https://www.sqlite.org/docs.html)

[Bootstrap_Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

