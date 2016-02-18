# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Views for Visiting

def visiting_list(request):
	visiting = (

		)
	return render(request, 'students/visiting_list.html',
		{'visiting': visiting})

def visiting_edit(request, vid):
	return HttpResponse('<h1>Edit Student %s</h1>' % vid)