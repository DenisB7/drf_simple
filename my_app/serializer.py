from rest_framework.serializers import ModelSerializer
from my_app.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']
