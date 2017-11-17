# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'current_total' not in request.session:
        request.session['current_total'] = 0
    if 'count' not in request.session:
        request.session['count'] = 0

    return render(request, "amadon/index.html")

def checkout(request):
    context = {
        'current_total': request.session['current_total'],
        'count': request.session['count'],
        'total': request.session['total']
    }
    return render(request, "amadon/checkout.html", context)

def process(request):
    if request.method != 'POST':
        return redirect('/amadon')
        
    quantity = int(request.POST['quantity'])
    product_id = int(request.POST['product_id'])

    if product_id == 101:
        request.session['current_total'] = (quantity * 19.99)
    elif product_id == 102:
        request.session['current_total'] = (quantity * 29.99)
    elif product_id == 103:
        request.session['current_total'] = (quantity * 4.99)
    elif product_id == 104:
        request.session['current_total'] = (quantity * 49.99)
    
    current_total = request.session['current_total']
    request.session['count'] += quantity
    request.session['total'] += current_total

    return redirect('/amadon/checkout')
