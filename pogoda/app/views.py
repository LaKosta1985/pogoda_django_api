import requests
from django.shortcuts import render
from app.forms import City_Form
from geopy.geocoders import Nominatim
access_key = "b03ac1f7-d589-4625-bfc8-56ac73fcce39"# ключ получен при регистрации на сервисе погоды Яндекс Api
headers = {
    "X-Yandex-Weather-Key": access_key
}
url = 'https://api.weather.yandex.ru/v2/forecast'

def index(request):
    if request.method=='POST':
        form =City_Form(request.POST)
        if form.is_valid():
           name=request.POST.get('name_City')
           geolocator = Nominatim(user_agent="Tester")
           adress = str(name)
           try:
                  location = geolocator.geocode(adress)
                  lat=location.latitude
                  lon=location.longitude
                  params = { 
                  'lat': lat, 
                  'lon': lon, 
                  'lang': 'ru_RU', # язык ответа 
                  'limit': 7, # срок прогноза в днях 
                  'hours': True, # наличие почасового прогноза 
                  'extra': False # подробный прогноз осадков 
                          } 
                  response = requests.get(url, params=params,headers=headers)
                  if response.status_code == 200:
                          data=response.json()
                  return render(request,"index.html",{'form':form,'data':data['fact'],'name':name,'title':"Температура"})
           except:
               form.add_error(None,"Нет данных по этому городу") 
        
    else:
        form=City_Form()  
    return render(request, "index.html",{'form':form,'title':"Температура"})  



