from django.db import models

# Create your models here.
class Book(models.Model):
    category_id = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.CharField(max_length=255)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title