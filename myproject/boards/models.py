from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=99, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
    subject = models.CharField(max_length=99)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete= models.CASCADE, related_name='topics')
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.subject

    def get_post_reply(self):
        return Post.objects.filter(topic__subject=self).count()-1
    
class Post(models.Model):
    message = models.TextField(max_length=250)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='post_topic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='post')
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE,null=True, related_name='+' )

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)


