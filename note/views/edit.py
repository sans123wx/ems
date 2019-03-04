from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import *

#删除记录
@login_required
def delete_note(request):
	user = request.user
	note_id = request.GET.get('note_id')
	note = Note.objects.get(id = note_id)
	if note.bzsj or user != note.owner:
		return render(request , 'note/404.html')
	else:
		note.delete()
		return redirect(reverse('manage_wbz'))

