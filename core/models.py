from django.db import models

# Create your models here.

class Teacher(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Parent(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Cook(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name
