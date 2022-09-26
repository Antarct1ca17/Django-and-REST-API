from django.shortcuts import render
import requests
import datetime
# Create your views here.

def index(request):
    if 'city' in request.GET:
        city = request.GET['city']
    else:
        city = 'London'

    appid = '5df4b1e5f7fa6f6c8bd4227ae316c7f7'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    res = requests.get(url=URL, params=PARAMS)

    if res.status_code == 200:
        res = requests.get(url=URL, params=PARAMS).json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temp = "{0:.1f}".format(res['main']['temp'])
        day = datetime.datetime.today()
        context = {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city}
    else: 
        context = {'description':'No info',  'temp':'No info', 'day':'No info', 'city':'No info'}       

    return render(request, 'weatherapp/index.html', context=context)