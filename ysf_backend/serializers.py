from .models import User
from rest_framework import serializers, validators




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'location', 'university', 'age_range', 'sdg_interest', 'attendance_type', 'accommodation_needed', 'academic_level', 'academic_major', 'how_hear_about_ysf', 'contact_preference', 'employment_status', 'expectations', 'shirt_size']





    