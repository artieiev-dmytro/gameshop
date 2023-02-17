from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return self.user.email

    def send_verification_email(self):
        link = reverse(
            "users:varify", kwargs={"email": self.user.email, "code": self.code}
        )
        verify_link = f"{settings.DOMAIN_NAME}{link}"
        subject = "GameShop"
        message = (
            f"Confirm the account {self.user.username} by clicking on {verify_link}"
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expirad(self):
        return True if now() >= self.expiration else False
