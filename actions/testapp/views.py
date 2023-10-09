"""Module dor views"""
from django.shortcuts import render


def ping(request):
    """Test view: ping-pong"""
    return render(request, 'testapp/index.html')
