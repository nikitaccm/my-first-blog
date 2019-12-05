from django.db import models
from django.utils import timezone


# Create your models here.

 #Post es el nombre del modelo y class define un objeto: models.Model: significa que post es un modelo de Django y q este debe guardarlo en BD
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #,models.ForeignKey este es una relación (link) con otro modelo.
    title = models.CharField(max_length=200) #models.CharField, así es como defines un texto con un número limitado de caracteres.
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField( # models.DateTimeField, este es fecha y hora.
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

