
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import render_template
from app import app
from flask_login import current_user


def send_mail(from_email, to_emails,
              plain_text_content, subject,
              html_content):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content,
        plain_text_content=plain_text_content
        )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return response

    except Exception as e:
        print(e)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(
               subject='[KingsKlass] Reset Your Password',
               from_email=app.config['ADMINS'][0],
               to_emails=[user.email],
               plain_text_content=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_content=render_template('email/reset_password.html',
                                         user=user, token=token))
