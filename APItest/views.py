from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse

def home(request):
    """return HttpResponse('Hello, World!')"""
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'home.html',{
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'api_key': '',
    })
    """, {'boards': boards})"""
