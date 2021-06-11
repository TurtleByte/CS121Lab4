from django.db import models

# Create your models here.

class Author(models.Model):
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    CountryOfOrigin = models.CharField(max_length=32)

    def __str__(self):
        return self.FirstName + " " + self.LastName

class Book(models.Model):
    BookTitle = models.CharField(max_length=128)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Category = models.CharField(max_length=32)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    NumberOfPages = models.PositiveIntegerField()
    Language = models.CharField(max_length=32)
