from django.db import models
class ContactData(models.Model):
    name= models.CharField(max_length=100)
    salary= models.IntegerField()
    email= models.EmailField(max_length=100)
    mobile= models.BigIntegerField()
    location= models.CharField(max_length=100)
