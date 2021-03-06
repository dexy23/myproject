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

# Views for Groups

def groups_list(request):
	groups = (
		{'id': 1,
		 'name': u'СЕКм-21',
		 'leader': {'id': 1, 'name': u'Феданяк Роман'}},
		{'id': 2,
		 'name': u'СЕКм-22',
		 'leader': {'id': 2, 'name': u'Притула Сергій'}},
		{'id': 3,
		 'name': u'СЕКм-23',
		 'leader': {'id': 3, 'name': u'Коваленко Олег'}},
		)
	return render(request, 'students/groups_list.html',
		{'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)