from django import forms
from .models import *

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['date' , 'lb' , 'xh' , 'gz' , 'jg' , 'sl' , 'dd' , 'fs' , 'sh' , 'sn' , 'shry' , 'shdh' , 'tzsj' , 'dxsj' , 'fxsj']
		widgets = {
				'date':forms.DateInput(attrs={'class':'form-control'}),
				'lb':forms.Select(attrs={'class':'form-control'}),
				'xh':forms.Select(attrs={'class':'form-control'}),
				'gz':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入故障描述'}),
				'jg':forms.NumberInput(attrs={'class':'form-control','placeholder':'请输入价格'}),
				'sl':forms.NumberInput(attrs={'class':'form-control','placeholder':'请输入数量'}),
				'dd':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入地点'}),
				'fs':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入处理的方式'}),
				'sh':forms.Select(attrs={'class':'form-control'}),
				'sn':forms.TextInput(attrs={'class':'form-control'}),
				'shry':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入售后人员'}),
				'shdh':forms.TextInput(attrs={'class':'form-control','placeholder':'请输入售后人员电话'}),
				'tzsj':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'dxsj':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'fxsj':forms.DateInput(attrs={'class':'form-control','type':'date'}),
		}