
from django.conf import settings
from django.core.mail import send_mail

def send_email(subject, message, recipients=[]):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipients)