from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import *
from django.db.models import *

#未报账
@login_required
def manage_wbz(request):
	user = request.user
	notes = Note.objects.filter(bz = False , owner = user)
	total_p = notes.aggregate(total_p = Sum('hj'))['total_p']
	unit_types = Unit_type.objects.filter(note__owner = user , note__bz = False).annotate(ut_p = Sum('note__hj'))
	context = {}
	context['notes'] = notes
	context['total_p'] = total_p
	context['unit_types'] = unit_types
	return render(request , 'note/management/manage_wbz.html' , context)

#已报账
@login_required
def manage_ybz(request):
	user = request.user
	notes = Note.objects.filter(bz = True , owner = user)
	total_p = notes.aggregate(total_p = Sum('hj'))['total_p']
	unit_types = Unit_type.objects.filter(note__owner = user , note__bz = True).annotate(ut_p = Sum('note__hj'))
	context = {}
	context['notes'] = notes
	context['total_p'] = total_p
	context['unit_types'] = unit_types
	return render(request , 'note/management/manage_ybz.html' , context)

#售后
@login_required
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

#类型
@login_required
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

#型号
@login_required
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

#密码
@login_required
def manage_mm(request):
	user = request.user
	if request.method == 'POST':
		psword = request.POST.get('password')
		user.set_password(psword)
		user.save()
		return redirect(reverse('login'))
	else:
		return render(request , 'note/management/manage_mm.html')