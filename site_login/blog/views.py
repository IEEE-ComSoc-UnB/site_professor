from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
    return render(request, 'blog/contact.html')

def index(request):
    return render(request, 'blog/index.html')

def form(request):
    return render(request, 'blog/form.html')