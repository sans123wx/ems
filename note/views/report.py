from ..models import *
from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse , FileResponse
from .functions import get_info , str_to_date , make_excel

#报账
@login_required
def bz(request):
	user = request.user
	groups = user.groups.all()
	list_groups = []
	#判断有无报账权限
	if (user.permissions.bz_dj or user.permissions.bz_wl or user.permissions.bz_jsj) and groups:
		#提交数据
		if request.method == "POST":
			#新建报账时间对象
			title = request.POST.get('title')
			date = str_to_date(request.POST.get('date'))
			customer_id = request.POST.get("sh")
			sh = Customer.objects.get(id = customer_id)
			new_report = Report_time()
			new_report.title = title
			new_report.bzsj = date
			new_report.sh = sh
			new_report.used = True
			new_report.save()
			#报账那记录
			notes_id = request.POST.getlist('ckb')
			for note_id in notes_id:
				note = Note.objects.get(id = note_id)
				note.bz = True
				note.bzsj = new_report
				note.save()
			return redirect(reverse('ybz_all'))
		#报账数据
		else:	
			if len(groups) == 1:
				customers = Customer.objects.filter(group = groups[0])
				notes = Note.objects.filter(sh = customers[0] , bz = False)
				list_groups.append(groups[0])
			else:
				list_groups , notes = get_info(user , groups)
			context = {}
			context['list_groups'] = list_groups
			context['notes'] = notes
			return render(request , 'note/report/bz.html' , context)
	else:
		return render(request , '404.html')

#报账页面的ajax
@login_required
def ajax_get_notes(request):
	customer_id = request.GET.get('customer_id')
	notes = Note.objects.filter(sh__id = customer_id , bz = False)
	context = {}
	context['notes'] = notes
	return render(request , 'note/report/ajax_get_notes.html' , context)

#打印页面
@login_required
def dy(request):
	notes_id = request.POST.getlist('ckb')
	list_notes = []
	for note_id in notes_id:
		note = Note.objects.get(id = note_id)
		list_notes.append(note)
	context = {}
	context['notes'] = list_notes
	return render(request , 'note/report/dy.html' , context)

@login_required
def download(request):
	if request.method == 'POST':
		notes_id = request.POST.getlist('ckb')
		customer_id = request.POST.get('sh')
		filename = make_excel(notes_id , customer_id)
		response = FileResponse(open(filename , 'rb') , as_attachment=True)
		return response
	else:
		return render(request , '404.html')


