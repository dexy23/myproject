# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Views for Students

def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Роман',
		 'last_name': u'Феданяк',
		 'ticket': 274,
		 'image': 'img/me.jpg'},
		 {'id': 2,
		 'first_name': u'Андрій',
		 'last_name': u'Василишин',
		 'ticket': 345,
		 'image': 'img/2.jpg'},
		 {'id': 3,
		  'first_name': u'Олег',
		  'last_name': u'Харитон',
		  'ticket': 376,
		  'image': 'img/3.gif'},
		 )
	return render(request, 'students/students_list.html', 
		{'students': students})

def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)