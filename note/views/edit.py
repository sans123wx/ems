from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import *
from ..forms import *
from .functions import edit_queryset

#删除记录
@login_required
def delete_note(request):
	user = request.user
	note_id = request.GET.get('note_id')
	note = Note.objects.get(id = note_id)
	if note.bzsj or user != note.owner:
		return render(request , 'note/404.html')
	else:
		note.delete()
		return redirect(reverse('manage_wbz'))

#修改记录
@login_required
def edit_note(request):
	user = request.user
	note_id = request.GET.get('note_id')
	if note_id:
		note = Note.objects.get(id = note_id)
		if request.method == 'POST':
			form = NoteForm(instance = note , data = request.POST)
			if form.is_valid():
				new_form = form.save(commit = False)
				if new_form.owner == user:
					new_form.save()
					return redirect(reverse('manage_wbz'))
				else:
					return render(request , 'note/404.html')
		else:
			form = NoteForm(instance = note)
			edit_queryset(user , form)
			context = {}
			context['form'] = form
			context['note_id'] = note_id
			return render(request , 'note/edit/edit_note.html' , context)
	else:
		return render(request , 'note/404.html')

#修改售后单位
@login_required
def edit_sh(request):
	owner = request.user
	groups = owner.groups.all()
	sh_id = request.GET.get('sh_id')
	if sh_id:
		sh = Customer.objects.get(id = sh_id)
		if request.method == 'POST':
			form = CustomerForm(instance = sh , data = request.POST)
			if form.is_valid():
				new_form = form.save(commit = False)
				if new_form.group in groups:
					new_form.save()
					return redirect(reverse('manage_sh'))
				else:
					return render(request , 'note/404.html')
		else:
			form = CustomerForm(instance = sh)
			form.fields['group'].queryset = groups
			context = {}
			context['form'] = form
			context['sh_id'] = sh_id
			return render(request , 'note/edit/edit_sh.html' , context)
	else:
		return render(request , 'note/404.html')

#修改设备类型
@login_required
def edit_lx(request):
	owner = request.user
	groups = owner.groups.all()
	lx_id = request.GET.get('lx_id')
	if lx_id:
		lx = Unit_type.objects.get(id = lx_id)
		if request.method == 'POST':
			form = Unit_typeForm(instance = lx , data = request.POST)
			if form.is_valid():
				new_form = form.save(commit = False)
				if new_form.sh.group in groups:
					new_form.save()
					return redirect(reverse('manage_lx'))
				else:
					return render(request , 'note/404.html')
		else:
			form = Unit_typeForm(instance = lx)
			if groups:
					for i in range(len(groups)):
						if i == 0:
							form.fields['sh'].queryset = Customer.objects.filter(group = groups[i])
						else:
							form.fields['sh'].queryset = form.fields['sh'].queryset.union(Customer.objects.filter(group = groups[i]))
			context = {}
			context['form'] = form
			context['lx_id'] = lx_id
			return render(request , 'note/edit/edit_lx.html' , context)
	else:
		return render(request , 'note/404.html')

#修改设备型号
@login_required
def edit_xh(request):
	owner = request.user
	groups = owner.groups.all()
	xh_id = request.GET.get('xh_id')
	if xh_id:
		xh = Unit_model.objects.get(id = xh_id)
		if request.method == 'POST':
			form = Unit_modelForm(instance = xh , data = request.POST)
			if form.is_valid():
				new_form = form.save(commit = False)
				if new_form.lx.sh.group in groups:
					new_form.save()
					return redirect(reverse('manage_xh'))
				else:
					return render(request , 'note/404.html')
		else:
			form = Unit_modelForm(instance = xh)
			if groups:
					for i in range(len(groups)):
						if i == 0:
							form.fields['lx'].queryset = Unit_type.objects.filter(sh__group = groups[i])
						else:
							form.fields['lx'].queryset = form.fields['lx'].queryset.union(Unit_type.objects.filter(sh__group = groups[i]))
			context = {}
			context['form'] = form
			context['xh_id'] = xh_id
			return render(request , 'note/edit/edit_xh.html' , context)
	else:
		return render(request , 'note/404.html')