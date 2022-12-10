from django.db import models


class Employee(models.Model):
    eid=models.CharField(max_length=50)
    ename=models.CharField(max_length=50)
    eemail=models.EmailField(max_length=50)

    class Meta:
        db_table='employee'
    