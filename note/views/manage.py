from django.shortcuts import render
from ..models import *

def my_note_wbz(request):
	return render(request , 'note/management/manage_wbz.html')