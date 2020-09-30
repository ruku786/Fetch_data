from django.db import models

class employee(models.Model):
    Name = models.CharField(max_length=50)
    Email_id = models.EmailField(max_length=50)
    Phone_no = models.CharField(max_length=11)
    def __str__(self):
        return self.name

# Create your models here.
