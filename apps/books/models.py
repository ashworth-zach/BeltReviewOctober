from __future__ import unicode_literals
from django.db import models
from ..users.models import *
# Create your models here.
class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['content']) < 10:
            errors["content"] = "content cannot be less than 10 characters"
        if len(postData['content']) > 200:
            errors["content"] = "content cannot be over 200 characters"
        if int(postData['rating'])>5 :
            errors["rating"] = "you cannot give a higher rating than 5"
        if int(postData['rating'])%.5 != 0:
            errors["rating"] = "you can only give ratings divisible by 0.5"
        return errors
class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "title cannot be less than 10 characters"
        if len(postData['title']) > 45:
            errors["title"] = "title cannot be over 45 characters"
        if len(postData['author']) < 5:
            errors["author"] = "author cannot be less than 5 characters"
        if len(postData['author']) > 45:
            errors["author"] = "author cannot be over 45 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "description cannot be less than 10 characters"
        if len(postData['desc']) > 200:
            errors["desc"] = "description cannot be over 200 characters"
        return errors
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BookManager()
class Review(models.Model):
    user=models.ForeignKey(User, related_name="reviews")
    book=models.ForeignKey(Book, related_name='books')
    rating=models.IntegerField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ReviewManager()