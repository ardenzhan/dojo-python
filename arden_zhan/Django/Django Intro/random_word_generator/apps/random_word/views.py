# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    if 'randomword' not in request.session:
        request.session['randomword'] = ""

    context = {
        'counter': request.session['counter'],
        'randomword': request.session['randomword']
    }
    return render(request, 'random_word/index.html', context)

def reset(request):
    request.session.flush()
    return redirect('/random_word')

def generate(request):
    request.session['randomword'] = get_random_string(length=14)
    request.session['counter'] += 1
    return redirect('/random_word')
    
    