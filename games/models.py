import stripe

from django.db import models
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    img = models.ImageField(upload_to="products_images", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=True)
    date = models.DateField()
    view = models.PositiveIntegerField(default=0)
    rating = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    stripe_game_price_id = models.CharField(max_length=128, blank=True, null=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.stripe_game_price_id:
            stripe_game_price_id = self.create_stripe_game_price()
            self.stripe_game_price_id = stripe_game_price_id["id"]
        super().save(*args, **kwargs)

    def create_stripe_game_price(self):
        stripe_game = stripe.Product.create(name=self.name)
        stripe_game_price = stripe.Price.create(
            product=stripe_game["id"],
            unit_amount=round(self.price * 100),
            currency="usd",
        )
        return stripe_game_price


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
