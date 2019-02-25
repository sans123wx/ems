from django.shortcuts import render , redirect
from ..models import *
from ..forms import *

def new_note(request):
	owner = request.user
	form = NoteForm()
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.owner = owner
			new_form.save()
			return redirect(reverse('manage_wbz'))
	else:
		groups = owner.groups.all()
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
