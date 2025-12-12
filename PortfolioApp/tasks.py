from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(name, email, message):
    subject = f"New Contact from {name}"
    body = f"Email: {email}\nMessage: {message}"

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        ['perumalragunandhan@gmail.com'],   # Where you want to receive emails
        fail_silently=False,
    )
