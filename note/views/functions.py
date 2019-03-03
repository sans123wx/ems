import datetime
from ..models import *
from django.contrib.auth.models import Group
from openpyxl import Workbook

#获取所有有报账权限的组
def get_info(user , groups):
	dict_permissions = {'电教部':user.permissions.bz_dj , '网络信息部':user.permissions.bz_wl , '计算机部':user.permissions.bz_jsj}
	list_groups = []
	for group in groups:
		if dict_permissions[group.name]:
			customers = Customer.objects.filter(group = group)
			list_groups.append(group)
	notes = Note.objects.filter(sh__group = list_groups[0] , bz = False)
	return list_groups , notes

#将时间格式装换成datetime.date类型
def str_to_date(date_str):
	list_date = date_str.split('-')
	date = datetime.date(int(list_date[0]) , int(list_date[1]) , int(list_date[2]))
	return date

#创建excel文件
def make_excel(notes_id , customer_id):
	group = Group.objects.get(customer__id = customer_id)
	filename = 'media/note/excel/%s.xlsx'%group.name
	wb = Workbook()
	ws = wb.active
	ws.append(['日期','类别','型号','价格','数量','总价','教室','售后'])
	for note_id in notes_id:
		note = Note.objects.get(id = note_id)
		ws.append([note.date , note.lb.title , note.xh.title , note.jg , note.sl , note.hj , note.dd , note.sh.title])
	wb.save(filename)
	return filename