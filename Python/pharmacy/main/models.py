from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	age = models.IntegerField()

	def __str__(self):
		return self.name

class Catalogue(models.Model):
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
	drug_name = models.CharField(max_length=200)
	date = models.DateField()
	price = models.IntegerField()
	gramm = models.IntegerField()
	description = models.CharField(max_length = 2000)

	def __str__(self):
		return self.drug_name

	def __str__(self):
		return self.description

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	drug = models.ForeignKey(Catalogue, on_delete=models.CASCADE)

class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	login = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

