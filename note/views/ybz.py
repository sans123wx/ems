from django.shortcuts import render , redirect
from django.urls import reverse
from ..models import *

def ybz_all(request):
	notes = Report_time.objects.all()
	context = {}
	context['notes'] = notes
	return render(request , 'note/show_notes/ybz/ybz_all.html' , context)

def ybz_dj(request):
	notes = Report_time.objects.filter(sh__group__name = '电教部')
	context = {}
	context['notes'] = notes
	return render(request , 'note/show_notes/ybz/ybz_dj.html' , context)

def ybz_wl(request):
	notes = Report_time.objects.filter(sh__group__name = '网络信息部')
	context = {}
	context['notes'] = notes
	return render(request , 'note/show_notes/ybz/ybz_wl.html' , context)

def ybz_jsj(request):
	notes = Report_time.objects.filter(sh__group__name = '计算机部')
	context = {}
	context['notes'] = notes
	return render(request , 'note/show_notes/ybz/ybz_jsj.html' , context)

def ybz_xx(request):
	report_id = request.GET.get('report_id')
	report_time = Report_time.objects.get(id = report_id)
	notes = Note.objects.filter(bzsj = report_id)
	context = {}
	context['notes'] = notes
	return render(request , 'note/show_notes/ybz/base_ybz_xx.html' , context)