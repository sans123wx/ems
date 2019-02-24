from django.urls import path
from .views import *

urlpatterns = [
		path('' , wbz_all , name = 'wbz_all'),
		path('wbz_dj' , wbz_dj , name = 'wbz_dj'),
		path('wbz_jsj' , wbz_jsj , name = 'wbz_jsj'),
		path('wbz_wl' , wbz_wl , name = 'wbz_wl'),
		#管理页面
		path('my_note_wbz' , my_note_wbz , name = 'my_note_wbz'),
]