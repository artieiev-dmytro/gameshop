from django.db import models

from users.models import User


class Order(models.Model):
    CREATED = 0
    PAIN = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUS = (
        (CREATED, "CREATED"),
        (PAIN, "PAIN"),
        (ON_WAY, "ON_WAY"),
        (DELIVERED, "DELIVERED"),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    cart_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUS)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orders №{self.id}. {self.first_name} {self.last_name}"

    def update_after_payment(self, cart_history):
        self.STATUS = self.PAIN
        self.cart_history = cart_history
        self.save()
