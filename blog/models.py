from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

def default_datetime():
        return timezone.now() + timedelta(hours=2)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default='Gaopalelwe Molekoa, Your Future Software Engineer')
    date = models.DateTimeField(default=default_datetime)
     
    
    def __str__(self):
        return self.title + ' | ' + str(self.signature)
    
    def get_absolute_url(self):
        return reverse('blog')
    
