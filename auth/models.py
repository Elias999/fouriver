from django.db import models

# Create your models here. databases models

class appusers(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    fullname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    idiotita = models.CharField(max_length=20)

    class Meta:
        db_table = "appusers"
