from django.db import models

# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'

    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    publishDate = models.DateField()
    edition = models.IntegerField()