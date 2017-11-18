# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# locations/money list in locations.py
from locations import locations
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    
    context = {
        'locations': locations
    }

    return render(request, "ninja_gold/index.html", context)

def process(request, location_name):
    result = {}

    for location in locations:
        if location['name'] == location_name:
            gold_change = randint(location['low'], location['high'])
            result['location_name'] = location_name
            result['gold_change'] = gold_change
            result['time'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")
            break
            
    try:
        request.session['activities']
    except KeyError: 
        request.session['activities'] = []

    temp = request.session['activities']
    temp.append(result)
    request.session['activities'] = temp

    request.session['total_gold'] += gold_change
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

