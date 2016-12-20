from django.db import models

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	status = models.IntegerField(default=1)