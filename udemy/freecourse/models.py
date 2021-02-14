from django.db import models

# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=400)
    fullname=models.CharField(max_length=1000,default="")
    Author=models.CharField(max_length=400)
    Code=models.CharField(max_length=200)
    url=models.CharField(max_length=400)


    def __str__(self):
        return f"{self.Name}"