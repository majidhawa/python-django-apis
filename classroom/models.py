from django.db import models

# Create your models here.

class Classroom(models.Model):
  class_name= models.CharField(max_length=20)
  number_of_seats= models.IntegerField()
  number_of_students= models.IntegerField()
  class_teacher= models.CharField(max_length=20)
  courses= models.CharField(max_length=25)
  available_equipments= models.TextField()
  description = models.TextField()
  
  def __str__(self):
      return f"{self.class_name}"
