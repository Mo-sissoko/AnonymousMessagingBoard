from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from website import db
from .models import Message

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def messageboard():
    if request.method == 'POST':
        message = request.form.get('message')
        if len(message) < 1:
            flash("You can't send an empty message！", category='error')
        elif len(message) > 128:
            flash("Your message is longer than 128 characters！", category='error')
        else:
            new_message = Message(message=message, user_id=current_user.id)
            db.session.add(new_message)
            db.session.commit()
            flash("New Message Added", category='success')
            return redirect(url_for('views.messageboard'))
    return render_template('messageboard.html', user=current_user,
                           messages=Message.query.order_by(Message.date.desc()).all())
