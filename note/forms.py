from django import forms
from .models import *

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['date' , 'sh', 'lb' , 'xh' , 'gz' , 'jg' , 'sl' , 'dd' , 'fs' , 'sn' , 'shry' , 'shdh' , 'tzsj' , 'dxsj' , 'fxsj']
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

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		widgets = {
				'title':forms.TextInput(attrs={'class':'form-control'}),
				'group':forms.Select(attrs={'class':'form-control'}),
		}

class Unit_typeForm(forms.ModelForm):
	class Meta:
		model = Unit_type
		fields = '__all__'
		widgets = {
				'title':forms.TextInput(attrs={'class':'form-control'}),
				'sh':forms.Select(attrs={'class':'form-control'}),
		}

class Unit_modelForm(forms.ModelForm):
	class Meta:
		model = Unit_model
		fields = ['title' , 'lx']
		widgets = {
				'title':forms.TextInput(attrs={'class':'form-control'}),
				'lx':forms.Select(attrs={'class':'form-control'}),
		}