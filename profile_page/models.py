from django.db import models

# Create your models here.
class profile(models.Model):
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    University = models.CharField(max_length=100)
    Email = models.CharField(max_length=100) 
    #Image = models.FileField(upload_to="profile_page/",max_length=250,null=True,default=None)

class add(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    filename = models.FileField(null=True)

class comment(models.Model):
    comment = models.CharField(max_length=200)
   
   
    
    