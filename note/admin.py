from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('date' , 'lb' , 'xh' , 'gz' , 'jg' , 'sl' , 'bz' , 'sh' ,
                    'hj' , 'zt' , 'owner' )

@admin.register(Unit_type)
class Unit_typeAdmin(admin.ModelAdmin):
    list_display = ('title' , 'sh' )

@admin.register(Unit_model)
class Unit_modelAdmin(admin.ModelAdmin):
    list_display = ('title' , 'lx' )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title' , 'group' )

@admin.register(Report_time)
class Report_timeAdmin(admin.ModelAdmin):
    list_display = ('title' , 'bz'  , 'bzsj' , 'sh' , 'used')
