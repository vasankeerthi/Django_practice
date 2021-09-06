from django.db import models

class Birthday(models.Model):
    name=models.CharField(max_length=150)
    dob=models.DateField()
    email=models.EmailField()
    def __str__(self):
        return self.name

    

# Create your models here.
