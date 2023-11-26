from django.db import models

# Create your models here.
class SurfingClass(models.Model):
    class_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    max_capacity = models.IntegerField(default=10)
    current_capacity = models.IntegerField(default=0)
    CLASS_TYPE_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('mixed', 'Mixed'),
    ]
    class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES, default='mixed')
    
    def available_spots(self):
        return self.max_capacity - self.current_capacity
    
class Booking(models.Model):
    surfing_class = models.ForeignKey(SurfingClass, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=100)
    contact_email = models.EmailField
    contact_number = models.CharField(max_length=20)