# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')
def process(request):
    if 'form_submit_number' not in request.session:
        request.session['form_submit_number'] = 0
    request.session['form_submit_number'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
def result(request):
    return render(request, 'survey/result.html')