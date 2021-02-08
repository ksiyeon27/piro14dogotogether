from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
import json
# Create your views here.



def showmap(request):
    with open('static/map/test.json', encoding='utf-8') as json_file:
        parks = json.load(json_file)
    parkdict = []
    for park in parks:
        if park.get('위도'):
            content = {
                "title": park['공원명'],
                "mapx": str(park['위도']),
                "mapy": str(park['경도']),
                "addr1": str(park['소재지지번주소']),
            }
            parkdict.append(content)
    API_KEY = getattr(settings, 'API_KEY', 'API_KEY')
    parkJson = json.dumps(parkdict, ensure_ascii=False)
<<<<<<< Updated upstream
    return render(request, 'map/showmap.html', {'parkJson': parkJson})

import json

def showanimalavail(request):
    with open('static/json/animalavail.json', encoding='utf-8') as json_file:
        places = json.load(json_file)['response']['body']['items']['item']

    places = []
    for place in places:
        if place.get('mapx'):
            content = {
                "title": place['title'],
                "mapx" : str(place['mapx']),
                "mapy" : str(place['mapy']),
                "address" : str(place['address']),
            }
            if place.get('tel'):
                content['tel'] = str(place['tel'])
            else:
                content['tel'] = ''
            places.append(content)
        placeJson = json.dumps(places, ensure_ascii=False)
        return render(request, 'map.html', {'placeJson': placeJson})
def testmap(request):
    with open('static/map/test.json', encoding='utf-8') as json_file:
        parks = json.load(json_file)
    parkdict = []
    for park in parks:
        if park.get('위도'):
            content = {
                "title": park['공원명'],
                "mapx": str(park['위도']),
                "mapy": str(park['경도']),
                "addr1": str(park['소재지지번주소']),
            }
            parkdict.append(content)
    parkJson = json.dumps(parkdict, ensure_ascii=False)
    return render(request, 'map/testmap.html', {'parkJson': parkJson})

# 위치 기반으로, 
=======
    return render(request, 'map/showmap.html', {'parkJson': parkJson, 'apiKey' : API_KEY})
>>>>>>> Stashed changes
