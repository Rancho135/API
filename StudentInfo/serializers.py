from django.db.models import fields
from rest_framework import serializers
from StudentInfo.models import StudentInfo


class StudentInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ["firstName","lastName","dateOfBirth","countryOfOrigin","studentCourse"]