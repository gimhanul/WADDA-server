from django.db import models
from django.db.models.fields.related import ForeignKey
from taggit.managers import TaggableManager
from django.db.models.deletion import CASCADE



#Question and Choice model
class Question(models.Model):
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10)

    def __str__(self):
        return self.choice



#Sight model
class Sight(models.Model):
    tags = TaggableManager(blank=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    time = models.CharField(max_length=11)
    tel = models.CharField(max_length=14)
    closed = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class SightImages(models.Model):
    sight = ForeignKey(Sight, on_delete=CASCADE)
    image = models.ImageField(upload_to='sights/')
