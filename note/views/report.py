from ..models import *

def get_info(user , groups):
	dict_permissions = {'电教部':user.permissions.bz_dj , '网络信息部':user.permissions.bz_wl , '计算机部':user.permissions.bz_jsj}
	list_info = {}
	for group in groups:
		if dict_permissions[group.name]:
			customers = Customer.objects.filter(group = groups)
			list_info[group] = customers
	notes = notes = Note.objects.filter(sh = list_info[groups[0]][0])
	return list_info , notes

def bz(request):
	user = request.user
	groups = user.groups.all()
	if (user.permission.bz_dj or user.permission.bz_wl or user.permission.bz_jsj) and groups:
		if len(groups) == 1:
			customers = Customer.objects.filter(group = groups[0])
			notes = Note.objects.filter(sh = customers[0])
			list_info = {group[0] , customers}
		else:
			list_info , notes = get_info(user , groups)
		context = {}
		context['list_info'] = list_info
		context['notes'] = notes
		return render(request , 'note/report/bz.html' , context)
	else:
		return render(request , '404.html')