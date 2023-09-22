from django.db import models

# Create your models here.
class student(models.Model):
    # id=models.AutoField() Automatically added
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)

# class product(models.Model):
#     pass

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return f"{self.car_name} {str(self.speed)}"
