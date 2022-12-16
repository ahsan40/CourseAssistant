from django.db import models

# Create your models here.

class content(models.Model):
    course_name = models.CharField(max_length=100,default='',null=False) 
    course_code = models.CharField(max_length=100,default='',null=False) 
    contributor = models.CharField(max_length=100,default='',null=False) 
    image = models.CharField(max_length=100,default='',null=False) 


class Content_request(models.Model):
    course_name = models.CharField(max_length=100,default='',null=False) 
    course_code = models.CharField(max_length=100,default='',null=False) 
    semester = models.CharField(max_length=100,default='',null=False) 
    description = models.CharField(max_length=300,default='',null=False)

