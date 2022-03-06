from django.db import models

class Book(models.Model):
    writer = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'