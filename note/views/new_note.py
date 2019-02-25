from django.shortcuts import render
from ..models import *

def new_note(request):
	return render(request , 'note/new_note/base_new_note.html')