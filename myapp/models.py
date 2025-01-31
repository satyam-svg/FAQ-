from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    published_date=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.title
