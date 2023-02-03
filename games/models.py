from django.db import models


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
    genge = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
