from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=99, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=99)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topic')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='topicuser')

    def __str__(self):
        return self.subject

class Post(models.Model):
    pass


class Company(models.Model):
    company = models.CharField(max_length=50, unique=True)
    founder = models.CharField(max_length=20)
    headquator = models.CharField(max_length=50)
    fund_raise = models.CharField(max_length=50)
    working = models.BooleanField(default=True)

    def __str__(self):
        return self.company

class Employee(models.Model):
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    address = models.CharField(max_length=99)
    experiance = models.CharField(max_length=99)
    Company = models.ForeignKey(Company, on_delete= CASCADE, related_name='employee')

    def __str__(self):
        return self.first_name+ "" + self.last_name

