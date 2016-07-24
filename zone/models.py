# coding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# class Post(models.Model):
    # author = models.ForeignKey(User)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
        # self.published_date = timezone.now()
        # self.save()

	# def __str__(self):
		# return self.title




class Tag(models.Model):
    class Meta:
        app_label = 'zone'
        verbose_name = '标签'
        verbose_name_plural = '标签'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
		
		
		

		
		

				
class Post(models.Model):
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
    # 作者
    author = models.ForeignKey(User)
    # 标题
    title = models.CharField(max_length=200)
    # 正文
    text = models.TextField()
    
    # 创建时间
    created_date = models.DateTimeField(default=timezone.now)
    # 发布时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title