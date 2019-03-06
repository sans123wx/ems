from django.shortcuts import render
from ..models import *
from django.contrib.auth.models import Group , User
from django.db.models import Sum

#所有部门未报账的记录
def wbz_all(request):
	notes = Note.objects.filter(bz = False)
	groups = Group.objects.filter(customer__note__bz = False).annotate(group_p = Sum('customer__note__hj'))
	total_p = groups.aggregate(total_p = Sum('group_p'))['total_p']
	context = {}
	context['notes'] = notes
	context['groups'] = groups
	context['total_p'] = total_p
	return render(request , 'note/show_notes/wbz/wbz_all.html' , context)

def wbz_dj(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '电教部')
	total_p = notes.aggregate(total_p = Sum('hj'))['total_p']
	unit_types = Unit_type.objects.filter(sh__group__name = '电教部' , note__bz = False).annotate(ut_p = Sum('note__hj'))
	context = {}
	context['notes'] = notes
	context['unit_types'] = unit_types
	context['total_p'] = total_p
	return render(request , 'note/show_notes/wbz/wbz_dj.html' , context)

def wbz_jsj(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '计算机部')
	total_p = notes.aggregate(total_p = Sum('hj'))['total_p']
	unit_types = Unit_type.objects.filter(sh__group__name = '计算机部' , note__bz = False).annotate(ut_p = Sum('note__hj'))
	context = {}
	context['notes'] = notes
	context['unit_types'] = unit_types
	context['total_p'] = total_p
	return render(request , 'note/show_notes/wbz/wbz_jsj.html' , context)

def wbz_wl(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '网络信息部')
	total_p = notes.aggregate(total_p = Sum('hj'))['total_p']
	unit_types = Unit_type.objects.filter(sh__group__name = '网络信息部' , note__bz = False).annotate(ut_p = Sum('note__hj'))
	context = {}
	context['notes'] = notes
	context['unit_types'] = unit_types
	context['total_p'] = total_p
	return render(request , 'note/show_notes/wbz/wbz_wl.html' , context)