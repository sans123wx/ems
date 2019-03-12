from django.urls import path
from .views import *

urlpatterns = [
		path('' , show_items , name = 'show_items'),
		path('ajax_process' , ajax_process , name = 'ajax_process'),
]