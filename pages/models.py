from django.db import models

# Create your models here.
class Home(models.Model):
    image = models.FileField(upload_to="face_image/", blank=True)
