from django.db import models
from django_countries.fields import CountryField



class victim(models.Model):
	first_name=models.CharField(max_length=200)
	last_name = models.CharField(max_length=30)
	Address_one = models.CharField(max_length=50)
	Address_two = models.CharField(max_length=50, blank=True)
	City = models.CharField(max_length=50)
	country = CountryField()
	zip_code = models.IntegerField()
	Email=models.CharField(max_length=50)
	password=models.CharField(max_length=80)
	card_number = models.IntegerField()
	card_expiry = models.IntegerField()
	card_cvc = models.IntegerField()
	
	
	def __str__(self):
	   	return self.Email


# Create your models here.
