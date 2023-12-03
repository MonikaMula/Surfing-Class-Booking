from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Classes(models.Model):
    DESCRIPTION = (('Mix', 'Mix'), ('Female', 'Female'), ('Male', 'Male'))
    CATEGORY = (('Beginner','Beginner'), ('Advance/Practicing', 'Advance/Practicing'))
    
    type = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, choices=DESCRIPTION)
    date_created = models.DateField(auto_now_add=True, null=True)


class Booking(models.Model):
    STATUS = (('PENDING BOOKING', 'PENDING BOOKING'), ('Waiting for approval', 'Waiting for approval'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'))
    
    booking_date = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    
    
# class SurfingClass(models.Model):
    # class_name = models.CharField(max_length=100)
    # instructor = models.CharField(max_length=100)
    # date = models.DateField()
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # location = models.CharField(max_length=200)
    # max_capacity = models.IntegerField(default=10)
    # current_capacity = models.IntegerField(default=0)
    # CLASS_TYPE_CHOICES = [
        # ('female', 'Female'),
        # ('male', 'Male'),
        # ('mixed', 'Mixed'),
    # ]
    # class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES, default='mixed')
    # 
    # def available_spots(self):
        # return self.max_capacity - self.current_capacity
    # 
    # def __str__(self):
        # return self.class_name
    # class Meta:
        # ordering = ["date", "start_time"]
    # 
# class Booking(models.Model):
    # surfing_class = models.ForeignKey(SurfingClass, on_delete=models.CASCADE)
    # participant_name = models.CharField(max_length=100)
    # contact_email = models.EmailField()
    # contact_number = models.CharField(max_length=20)
    # 
    # def __str__(self):
        # return f"Booking for {self.surfing_class} by {self.participant_name}"
    # class Meta:
        # ordering = ["surfing_class", "participant_name"]