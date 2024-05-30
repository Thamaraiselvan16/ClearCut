from django.db import models

class Image(models.Model):
    original_name = models.CharField(max_length=255)
    rembg_name = models.CharField(max_length=255)
    image_data = models.BinaryField()
    timestamp = models.DateTimeField(auto_now_add=True)
