from django.shortcuts import render

def index(request):
	context = {}
	return render(request, 'static_pages/index.html', context)

def events(request):
	context = {}
	return render(request, 'static_pages/events.html', context)

def projects(request):
	context = {}
	return render(request, 'static_pages/projects.html', context)

def startups(request):
	context = {}
	return render(request, 'static_pages/startups.html', context)
