from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Usedtrading(models.Model):
    
    writer = models.CharField(max_length = 200, default='')
    title = models.CharField(max_length = 200)
    cost = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    images = models.ImageField(blank = True, upload_to = "images",null = True)
    image2 = models.ImageField(blank = True, upload_to = "image2",null = True)
    image3 = models.ImageField(blank = True, upload_to = "image3",null = True)
    image_thumbnail = ImageSpecField(source = 'images', processors = [ResizeToFill(120,80)], format='JPEG')
    #
    if images.width_field == 0:
        pass
    if image2.width_field == 0:
        pass
    if image3.width_field == 0:
        pass
    
    def thumbnail(self):
        #썸네일 사진도 요약에 넣자
        return self.images

    def __str__(self):
        return self.title

    #100글자 제한해서 게시글 요약 보기
    def summary(self):
        return self.body[:50]