import requests
from django.shortcuts import HttpResponse
from app_proyecto.models import Stations

def funcion(z,val):
    if 'val' in z:
        valor = True
    else:
        valor = False    
    return valor

def insert_stations(request):
    
    url = "http://api.citybik.es/v2/networks/bikesantiago"
    json_data = requests.get(url).json()  
    #print(json_data)
    keysList = list(json_data.values())

    for i in range(0,224):
        Stations.objects.create(
            id_primary = keysList[0]['stations'][i]['id'],
            name_station =  keysList[0]['stations'][i]['name'],
            address =  keysList[0]['stations'][i]['extra']['address'],
            empty_slot = keysList[0]['stations'][i]['empty_slots'],                                          
            altitude =  keysList[0]['stations'][i]['extra']['altitude'],
            ebikes = keysList[0]['stations'][i]['extra']['ebikes'],
            has_ebikes = keysList[0]['stations'][i]['extra']["has_ebikes"],
            last_updated = keysList[0]['stations'][i]['extra']['last_updated'],
            normal_bikes = keysList[0]['stations'][i]['extra']['normal_bikes'],
            payment_key = funcion(keysList[0]['stations'][i]['extra']['payment'], 'key'),
            payment_transitcard = funcion(keysList[0]['stations'][i]['extra']['payment'], 'transitcard'),
            payment_creditcard = funcion(keysList[0]['stations'][i]['extra']['payment'], 'creditcard'),
            payment_phone = funcion(keysList[0]['stations'][i]['extra']['payment'], 'phone'),
            #post_code = models.Int(10)
            renting = keysList[0]['stations'][i]['extra']['renting'],
            returning_val = keysList[0]['stations'][i]['extra']['returning'],
            slots = keysList[0]['stations'][i]['extra']['slots'],
            uid = keysList[0]['stations'][i]['extra']['uid'],
            free_bikes = keysList[0]['stations'][i]['free_bikes'],
            latitude = keysList[0]['stations'][i]['latitude'],
            longitude = keysList[0]['stations'][i]['longitude'],
            )
    return HttpResponse('Todo salio bien')
# Create your views here.
