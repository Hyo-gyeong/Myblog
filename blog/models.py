from django.db import models
from datetime import datetime
from imagekit.models import ImageSpecField # 썸네일 만들 수 있게 해줌
from imagekit.processors import ResizeToFill # 썸네일 크기 조정

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images/', null=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(80, 80)])
    body = models.TextField()

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:200]