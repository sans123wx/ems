from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ..models import *
from ..forms import *

@login_required
def new_note(request):
	owner = request.user
	groups = owner.groups.all()
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.owner = owner
			if new_form.sh.group in groups:
				new_form.save()
				return redirect(reverse('manage_wbz'))
			else:
				return render(request , 'note/404.html')
	else:
		form = NoteForm()
		if groups:
			for i in range(len(groups)):
				if i == 0:
					form.fields['sh'].queryset = Customer.objects.filter(group = groups[i])
				else:
					form.fields['sh'].queryset = form.fields['sh'].queryset.union(Customer.objects.filter(group = groups[i]))
			for i in range(len(groups)):
				if i == 0:
					form.fields['lb'].queryset = Unit_type.objects.filter(sh__group = groups[i])
				else:
					form.fields['lb'].queryset = form.fields['lb'].queryset.union(Unit_type.objects.filter(sh__group = groups[i]))
			for i in range(len(groups)):
				if i == 0:
					form.fields['xh'].queryset = Unit_model.objects.filter(lx__sh__group = groups[i])
				else:
					form.fields['xh'].queryset = form.fields['xh'].queryset.union(Unit_model.objects.filter(lx__sh__group = groups[i]))
		context = {}
		context['form'] = form
		return render(request , 'note/new_note/new_note.html' , context)

def ajax_get_unit_types(request):
	customer_id = request.GET.get('customer_id')
	unit_types = Unit_type.objects.filter(sh__id = customer_id)
	context = {}
	context['unit_types'] = unit_types
	return render(request , 'note/new_note/ajax_get_unit_types.html' , context)

def ajax_get_unit_models(request):
	unit_type_id = request.GET.get('unit_type_id')
	unit_models = Unit_model.objects.filter(lx__id = unit_type_id)
	context = {}
	context['unit_models'] = unit_models
	return render(request , 'note/new_note/ajax_get_unit_models.html' , context)

@login_required
def new_customer(request):
	owner = request.user
	groups = owner.groups.all()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit = False)
			if new_form.group in groups:
				new_form.save()
				return redirect(reverse('new_note'))
			else:
				return render(request , 'note/404.html')
	else:
		form = CustomerForm()
		form.fields['group'].queryset = groups
		context = {}
		context['form'] = form
		return render(request , 'note/new_note/new_customer.html' , context)

@login_required
def new_unit_type(request):
	owner = request.user
	groups = owner.groups.all()
	if request.method == 'POST':
		form = Unit_typeForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit = False)
			if new_form.sh.group in groups:
				new_form.save()
				return redirect(reverse('new_note'))
			else:
				return render(request , 'note/404.html')
	else:
		form = Unit_typeForm()
		if groups:
				for i in range(len(groups)):
					if i == 0:
						form.fields['sh'].queryset = Unit_type.objects.filter(sh__group = groups[i])
					else:
						form.fields['sh'].queryset = form.fields['sh'].queryset.union(Unit_type.objects.filter(sh__group = groups[i]))
		context = {}
		context['form'] = form
		return render(request , 'note/new_note/new_unit_type.html' , context)

@login_required
def new_unit_model(request):
	owner = request.user
	groups = owner.groups.all()
	if request.method == 'POST':
		form = Unit_modelForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit = False)
			if new_form.lx.sh.group in groups:
				new_form.save()
				return redirect(reverse('new_note'))
			else:
				return render(request , 'note/404.html')
	else:
		form = Unit_modelForm()
		if groups:
				for i in range(len(groups)):
					if i == 0:
						form.fields['lx'].queryset = Unit_model.objects.filter(lx__sh__group = groups[i])
					else:
						form.fields['lx'].queryset = form.fields['lx'].queryset.union(Unit_model.objects.filter(lx__sh__group = groups[i]))
		context = {}
		context['form'] = form
		return render(request , 'note/new_note/new_unit_model.html' , context)
