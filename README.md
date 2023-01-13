# Anonymous Messaging Board

## Description

This is a simple anonymous messaging board. It is a simple web application that allows users to post messages to a
message board. The messages are displayed on the message board from most recent to less recent. The messages are
anonymous. 

## High-Level Overview

The application is written in Python and uses the Flask microframework. The application uses a SQLite database to
store the messages. The application is written in a modular fashion. The application consists of a single file
`main.py` that contains the Flask application. The application also contains a `models.py` file that contains the
database models, a `auth.py` file that contains the authentication logic (Logging in and Signing up), a `——init——.py` file that contains the
application factory, a `templates` directory that contains the HTML templates, a `utils.py` file that contains
utility functions, and a `views.py` file that contains the logic for the message board view. I also used Bootstrap for
styling. Both `views.py` and `auth.py` interact with the database using the models defined in `models.py`.

# Why I fufilled the requirements

Requirements:
* Users should be able to type a message and post it to the message board.
  * The message must be non-empty, and at most 128 characters long.
* Users should be able to see messages on the message board from most to least recent.
* Users on different computers should be able to post to the same board and view each other’s messages.

I fufilled the requirements because in my application, users can type a message that is non-empty and at most 128. The
message is then posted to the message board. The messages are displayed on the message board from most recent to least recent.
The messages are anonymous.

# Additional Features
Additional features that I implemented include:
* Data persistence
* User authentication
* User registration
* User login
* User logout
* User password hashing
## Installation

1. Install Python 3.7 or higher.
2. Install the Python dependencies using the following command:

    python -m pip install -r requirements.txt

3. Run the application using the following command:

    python main.py

## Usage

1. Open a web browser and navigate to `http://localhost:5000/`.
2. Login or Sign up, if you do not have an account.
3. Type a message in the text box and click the `Send` button.
4. The message is displayed on the message board.

## License

This software is released under the MIT License.

## Author

This software was written by [Mouhamadou Sissoko](mailto:mouhamadou708@gmail.com)
