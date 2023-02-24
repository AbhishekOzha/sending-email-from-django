from django.conf import settings
from django.core.mail import send_mail
def send_email_test(email):
    subject = 'please come online'
    message = f'you are selected.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )