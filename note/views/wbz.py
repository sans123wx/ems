from django.shortcuts import render
from ..models import *

#所有部门未报账的记录
def wbz_all(request):
	notes = Note.objects.filter(bz = False)
	content = {}
	content['notes'] = notes
	return render(request , 'note/show_notes/wbz_all.html' , content)

def wbz_dj(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '电教部')
	content = {}
	content['notes'] = notes
	return render(request , 'note/show_notes/wbz_dj.html' , content)

def wbz_jsj(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '计算机部')
	content = {}
	content['notes'] = notes
	return render(request , 'note/show_notes/wbz_jsj.html' , content)

def wbz_wl(request):
	notes = Note.objects.filter(bz = False , sh__group__name = '网络信息部')
	content = {}
	content['notes'] = notes
	return render(request , 'note/show_notes/wbz_wl.html' , content)