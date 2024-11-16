from django.db import models

# Create your models here.
class Speaker(models.Model):
    spker_name = models.CharField(max_length=100)
    speaker_qt = models.CharField(max_length=100)
    spker_desc = models.CharField(max_length=100)
    spker_img = models.ImageField(upload_to="spkerimgs/")