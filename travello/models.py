from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    Offer = models.BooleanField(default=False)