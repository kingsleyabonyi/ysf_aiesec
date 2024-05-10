from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    age_range = models.CharField(max_length=10)
    sdg_interest = models.CharField(max_length=100)
    attendance_type = models.CharField(max_length=100)
    # accommodation_needed = models.BooleanField()
    academic_level = models.CharField(max_length=50)
    academic_major = models.CharField(max_length=100)
    how_hear_about_ysf = models.CharField(max_length=200)
    contact_preference = models.CharField(max_length=200)
    employment_status = models.CharField(max_length=100)
    expectations = models.TextField()
    shirt_size = models.CharField(max_length=100)



    def __str__(self):
        return self.first_name


