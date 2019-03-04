from .wbz import *
from .manage import *
from .new_note import *
from .report import *
from .ybz import *
from .edit import *
from ..models import Note

def ajax_get_notes_detail(request):
	note_id = request.GET.get('note_id')
	note = Note.objects.get(id = note_id)
	context = {}
	context['note'] = note
	return render(request , 'note/note_detail.html' , context) 
