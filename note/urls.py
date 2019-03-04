from django.urls import path
from .views import *

urlpatterns = [
		#未报账
		path('' , wbz_all , name = 'wbz_all'),
		path('wbz_dj' , wbz_dj , name = 'wbz_dj'),
		path('wbz_jsj' , wbz_jsj , name = 'wbz_jsj'),
		path('wbz_wl' , wbz_wl , name = 'wbz_wl'),
		#已报账
		path('ybz_all' , ybz_all , name = 'ybz_all'),
		path('ybz_dj' , ybz_dj , name = 'ybz_dj'),
		path('ybz_wl' , ybz_wl , name = 'ybz_wl'),
		path('ybz_jsj' , ybz_jsj , name = 'ybz_jsj'),
		#已报账详细信息
		path('ybz_xx' , ybz_xx , name = 'ybz_xx'),
		#管理页面
		path('manage_wbz' , manage_wbz , name = 'manage_wbz'),
		path('manage_sh' , manage_sh , name = 'manage_sh'),
		path('manage_lx' , manage_lx , name = 'manage_lx'),
		path('manage_xh' , manage_xh , name = 'manage_xh'),
		#新增记录
		path('new_note' , new_note , name = 'new_note'),
		path('new_customer' , new_customer , name = 'new_customer'),
		path('new_unit_type' , new_unit_type , name = 'new_unit_type'),
		path('new_unit_model' , new_unit_model , name = 'new_unit_model'),
		#x新增记录ajax
		path('ajax_get_unit_types' , ajax_get_unit_types , name = 'ajax_get_unit_types'),
		path('ajax_get_unit_models' , ajax_get_unit_models , name = 'ajax_get_unit_models'),
		#报账
		path('bz' , bz , name = 'bz'),
		#打印页面
		path('dy' , dy , name = 'dy'),
		#下载页面
		path('download' , download , name = 'download'),
		#报账界面ajax获取notes
		path('ajax_get_notes' , ajax_get_notes , name = 'ajax_get_notes'),
		#获取记录详细信息
		path('ajax_get_notes_detail' , ajax_get_notes_detail , name = 'ajax_get_notes_detail'),
]