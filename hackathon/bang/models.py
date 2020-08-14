from django.db import models
from imagekit.models import ImageSpecField, ImageField
from imagekit.processors import ResizeToFill

# Create your models here.
def Bang(models.Model) :
    writer = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    roomtype = models.IntegerField()
    # cost = models.TextField()
    # image = imagekit.models.ImageField(blank=True, upload_to="images", null=True)
    # image2 = imagekit.models.ImageField(blank=True, upload_to="images2", null=True)
    # image3 = imagekit.models.ImageField(blank=True, upload_to="images3", null=True)
    # image_thumbnail = ImageSpecField(source='images', processors=[ResizeToFill(120, 80)], format='JPEG')

    if images.width_field == 0:
        pass

    def thumbnail(self):
        return self.images

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]