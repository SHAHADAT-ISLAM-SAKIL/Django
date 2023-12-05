from django.db import models

# Create your models here.
class StudentModels(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key= True)
    father_name = models.CharField(max_length= 30)
    address = models.TextField()
    
    def __str__(self):
        return f"name : {self.name} roll : {self.roll} Father name : {self.father_name} Address : {self.address}"
