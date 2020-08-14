from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail
from imagekit.processors import ResizeToFill

# Create your models here.
class Bang(models.Model) :
    writer = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    cost = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    roomtype = models.IntegerField()
    posision = models.CharField(max_length=300, null=False, default="")
    images = models.ImageField(blank=True, upload_to="images", null=True)
    image2 = models.ImageField(blank=True, upload_to="images2", null=True)
    image3 = models.ImageField(blank=True, upload_to="images3", null=True)
    image_thumbnail = ImageSpecField(source='images', processors=[ResizeToFill(120, 80)], format='JPEG')

    if images.width_field == 0:
        pass

    def thumbnail(self):
        return self.images

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]