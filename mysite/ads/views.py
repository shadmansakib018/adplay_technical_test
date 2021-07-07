from django.shortcuts import render
from .models import AdtrackTest
# Create your views here.
def home(request) :
	return render(request, 'ads/home.html', {
		'ads': AdtrackTest.objects.all()[0:100]
		})