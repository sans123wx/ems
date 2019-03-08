from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Item(models.Model):
	title = models.CharField(max_length = 50 , verbose_name = '项目名称')

class Item_process(models.Model):
	item = models.ForeignKey(Item ,verbose_name = '所属项目' , on_delete = models.DO_NOTHING)
	title = models.CharField(max_length = 50 , verbose_name = '名称')
	text = RichTextUploadingField(verbose_name = '内容')

