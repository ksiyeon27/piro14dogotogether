from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
import json
from .models import placeAddByUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


def showmap(request):
    with open('static/map/parks.json', encoding='utf-8') as json_file:
        parks = json.load(json_file)
    parkdict = []
    for park in parks:
        if park.get('이름'):
            content = {
                "title": (park['이름']),
                "mapx": str(park['위도']),
                "mapy": str(park['경도']),
                "addr1": str(park["기타"])
            }
            parkdict.append(content)
    API_KEY = getattr(settings, 'API_KEY', 'API_KEY')
    parkJson = json.dumps(parkdict, ensure_ascii=False)

    placedict=[]
    places = placeAddByUser.objects.all()
    for place in places:
        content= {
            "title":place.name,
            "mapx":str(place.xmap),
            "mapy":str(place.ymap),
            "author":str(place.created_by),
        }
        placedict.append(content)
    
    placeJson = json.dumps(placedict, ensure_ascii=False)
    user={'user':str(request.user)}
    userJson=json.dumps(user)

    return render(request, 'map/showmap.html', {'parkJson': parkJson, 'API_KEY' : API_KEY,'placeJson':placeJson,'userJson':userJson})

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

@csrf_exempt
def addplace(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        new_place=placeAddByUser()
        new_place.name=req['title']
        new_place.xmap=req['xmap']
        new_place.ymap=req['ymap']
        new_place.created_by=request.user
        new_place.save()
        return JsonResponse({'id': str(new_place.id)})
    elif request.method == 'GET':
        return render(request, 'base.html')


@csrf_exempt
def deleteplace(request):
    if request.method=='POST':
       req = json.loads(request.body)
       title=req['title']
       place=placeAddByUser.objects.filter(name=title).first()
       place.delete()
       return JsonResponse({'id': str(title)})
    
    elif request.method == 'GET':
        return render(request, 'base.html')
