from django.db import models

# Create your models here.
class SurfingClass(model.Model):
    class_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    max_capacity = models.IntegerField()
    current_capacity = models.IntegerField(default=0)
    
    def available_spots(self):
        return self.max_capacity - self.current_capacity