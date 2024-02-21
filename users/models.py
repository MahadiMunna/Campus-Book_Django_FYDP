from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    university = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    present_address = models.CharField(max_length=200)
    premanent_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"