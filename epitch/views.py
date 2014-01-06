from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from epitch.forms import *
def index(request):
	return render(request, 'epitch/index.html', {})

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/epitch/submit/')
	else:
		form = RegistrationForm() 

	return render(request, 'epitch/register.html', {'form': form})

def submit(request):
	return HttpResponse("Thank you for Registering.")