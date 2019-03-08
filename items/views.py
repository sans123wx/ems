from django.shortcuts import render
from .models import *
# Create your views here.

def show_items(request):
	item = Item.objects.first()
	context = {}
	context['item'] = item
	return render(request , 'items/show_items.html' , context)

def ajax_process(request):
	process_id = request.GET.get('process_id')
	process = Item_process.objects.get(id = process_id)
	context = {}
	context['process'] = process
	return render(request , 'items/ajax_process.html' , context)