from ..models import *
from django.shortcuts import render

def get_info(user , groups):
	dict_permissions = {'电教部':user.permissions.bz_dj , '网络信息部':user.permissions.bz_wl , '计算机部':user.permissions.bz_jsj}
	list_groups = []
	for group in groups:
		if dict_permissions[group.name]:
			customers = Customer.objects.filter(group = group)
			list_groups.append(group)
	notes = Note.objects.filter(sh__group = list_groups[0])
	return list_groups , notes

def bz(request):
	user = request.user
	groups = user.groups.all()
	list_groups = []
	if (user.permissions.bz_dj or user.permissions.bz_wl or user.permissions.bz_jsj) and groups:
		if len(groups) == 1:
			customers = Customer.objects.filter(group = groups[0])
			notes = Note.objects.filter(sh = customers[0])
			list_groups.append(groups[0])
		else:
			list_groups , notes = get_info(user , groups)
		context = {}
		context['list_groups'] = list_groups
		context['notes'] = notes
		return render(request , 'note/report/bz.html' , context)
	else:
		return render(request , '404.html')