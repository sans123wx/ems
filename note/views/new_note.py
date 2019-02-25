from django.shortcuts import render
from ..models import *
from ..forms import *

def new_note(request):
	owner = request.user
	form = NoteForm()
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