from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import AbstractUser

sizes = [('38', '38'), ('39', '39'), ('40','40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45')]

class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)

class Category(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f'{self.name.title()}'

class Size(models.Model):
    size = models.CharField(max_length=2, choices=sizes)

    def __str__(self):
        return self.size

class Cloth(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    new = models.BooleanField()
    sizes = models.ManyToManyField(Size)
    image = models.ImageField(upload_to='cloth_images/', blank=True, null=True)
    basket = models.ManyToManyField(User, related_name="save_cloth", blank=True)


    def __str__(self):
        return f'{self.name.title()}'

