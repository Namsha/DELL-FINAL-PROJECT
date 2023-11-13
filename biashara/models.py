from django.db import models


# Create your models here.

class Member(models.Model):
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=36)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(0)
    description = models.TextField()
    origin = models.CharField(max_length=50,default="kenya")
    color = models.CharField(max_length=30,default="white")

    def __str__(self):
        return self.name + " " + str(self.price)

