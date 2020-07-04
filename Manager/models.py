from django.db import models

class User(models.Model):
	name = models.TextField(max_length=100)
	password = models.TextField(max_length=100)
# Create your models here.
