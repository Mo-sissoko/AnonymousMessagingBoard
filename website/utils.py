import re

from flask import flash


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def check_password_strength(password):
    if len(password) < 8:
        flash('Password must be at least 8 characters.', category='error')
        return False
    elif not re.search("[a-z]", password):
        flash('Password must contain at least one lowercase letter.', category='error')
        return False
    elif not re.search("[A-Z]", password):
        flash('Password must contain at least one uppercase letter.', category='error')
        return False
    elif not re.search("[0-9]", password):
        flash('Password must contain at least one number.', category='error')
        return False
    elif not re.search("[!@#\$%^&*]", password):
        flash('Password must contain at least one special character.', category='error')
        return False

    return True
