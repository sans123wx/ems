from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Item_process)
class Item_processAdmin(admin.ModelAdmin):
	list_display = ['item' , 'title' , 'text']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ['title']