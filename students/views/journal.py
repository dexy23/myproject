# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Views for Visiting

def journal_list(request):
	journal = (
		{'id': 1,
		 'name': u'Василишин Андрій'},
		{'id': 2,
		 'name': u'Феданяк Роман'},
		{'id': 3,
		 'name': u'Харитон Олег'},		
		)
	return render(request, 'students/journal_list.html',
		{'journal': journal})

def journal_edit(request, vid):
	return HttpResponse('<h1>Edit Student %s</h1>' % vid)