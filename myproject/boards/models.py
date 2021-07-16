from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=99, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=99)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete= models.CASCADE, related_name='topics')

    def __str__(self):
        return self.subject

class Post(models.Model):
    post_message = models.TextField(max_length=250)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='post')
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE,null=True, related_name='+' )

    def __str__(self):
        return self.post_message


