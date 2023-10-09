"""Module dor views"""
from django.http import HttpResponse


def ping(request):
    """Test view: ping-pong"""
    return HttpResponse('pong')
