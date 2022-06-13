from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='作者')
    title=models.CharField(max_length=100,verbose_name='标题')
    text=models.TextField(verbose_name='正文')
    created_date=models.DateTimeField(default=timezone.now,verbose_name='编辑时间')
    published_date=models.DateTimeField(blank=True,null=True,verbose_name='发布时间')
    def publish(self):
        self.published_date=auto_now_add=True()
        self.save()
    def __str__(self):
        return self.title