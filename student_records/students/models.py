from django.db import models

# Create your models here.
class Student(models.Model):
    student_ID = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return f"student {self.first_name} {self.last_name}"
