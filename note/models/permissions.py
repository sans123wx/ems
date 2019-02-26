from django.db import models
from django.contrib.auth.models import User

class Permissions(models.Model):
	user = models.OneToOneField(User , on_delete = models.DO_NOTHING , verbose_name = '用户')
	bz_dj = models.BooleanField(default = False , verbose_name = '电教部报账权限')
	bz_wl = models.BooleanField(default = False , verbose_name = '网络信息部报账权限')
	bz_jsj = models.BooleanField(default = False , verbose_name = '计算机部报账权限')

	class Meta:
		verbose_name = '权限'
		verbose_name_plural = '权限'
	
