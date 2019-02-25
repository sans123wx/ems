from django.shortcuts import render
from ..models import *

def manage_wbz(request):
	user = request.user
	notes = Note.objects.filter(bz = False , owner = user)
	context = {}
	context['notes'] = notes
	return render(request , 'note/management/manage_wbz.html' , context)

def manage_sh(request):
	user = request.user
	groups = user.groups.all()
	customers = []
	for group in groups:
		customer = Customer.objects.filter(group = group)
		for c in customer:
			customers.append(c)
	context = {}
	context['notes'] = customers
	return render(request , 'note/management/manage_sh.html' , context)

def manage_lx(request):
	user = request.user
	groups = user.groups.all()
	unit_types = []
	for group in groups:
		unit_type = Unit_type.objects.filter(sh__group = group)
		for u in unit_type:
			unit_types.append(u)
	context = {}
	context['notes'] = unit_types
	return render(request , 'note/management/manage_lx.html' , context)

def manage_xh(request):
	user = request.user
	groups = user.groups.all()
	unit_models = []
	for group in groups:
		unit_model = Unit_model.objects.filter(lx__sh__group = group)
		for m in unit_model:
			unit_models.append(m)
	context = {}
	context['notes'] = unit_models
	return render(request , 'note/management/manage_xh.html' , context)