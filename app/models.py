from django.db import models

# Create your models here.
class College(models.Model):
    Cname=models.CharField(max_length=100)
    Cprincipal=models.CharField(max_length=100)
    Clocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Cname