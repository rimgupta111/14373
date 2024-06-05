from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=100,default='',null=True)
    last_name = models.CharField(max_length=100,default='',null=True)
    email = models.CharField(max_length=100,default='',null=True)
    password = models.CharField(max_length=100,default='',null=True)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.first_name


