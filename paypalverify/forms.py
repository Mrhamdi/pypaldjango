from django import forms
from .models import victim



class addvictim(forms.ModelForm):
	class Meta:
		model= victim
		fields =['first_name','last_name','Address_one','Address_two','City','country','zip_code','Email','password','card_number','card_expiry','card_cvc']