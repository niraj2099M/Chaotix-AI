from django.db import models

# Create your models here.
class ImageMetadata(models.Model):
    prompt = models.TextField(null=True)
    image_generated = models.ImageField(upload_to="images_generated/",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt}"