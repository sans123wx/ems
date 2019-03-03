from django.shortcuts import render , redirect
from django.urls import reverse
from ..models import *

def ybz_all(request):
	notes = Report_time.objects.all()
	context = {}
	context['notes'] = notes
	return render(request , 'note/ybz/ybz_all.html' , context)