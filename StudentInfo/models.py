from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
from django.utils import timezone
from django .contrib.auth import get_user_model
from django.contrib.auth.models import User

#User = get_user_model()
class StudentInfo(models.Model):
    firstName=models.CharField(max_length=20,blank=True)
    lastName=models.CharField(max_length=20,blank=True)
    studentId = models.ForeignKey(User, on_delete =models.CASCADE,related_name='user', max_length=100)
    dateOfBirth=models.DateField(max_length=50)
    countryOfOrigin=models.CharField(max_length=20)
    studentCourse=models.CharField(max_length=20)

    