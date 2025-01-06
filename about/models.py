from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    bio = models.TextField()
    # updated_on = models.DateTimeField(auto_now=True)