from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
import json
from .models import placeAddByUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


def showmap(request):
    with open('map/static/map/etc.json', encoding='utf-8') as json_file:
        etcs = json.load(json_file)   
    
    with open('map/static/map/data.json', encoding='utf-8') as json_file:
        datas = json.load(json_file)
    
    parkdict = []
    cafedict = []
    bistrodict = []
    etcdict=[]

    for data in datas:
        if data['종류'] == "식당":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category":str(data['종류']),
            }
            bistrodict.append(content)
        if data['종류'] == "카페":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category":str(data['종류']),
            }
            cafedict.append(content)
        if data['종류'] == "공원":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category": str(data['종류']),
            }
            parkdict.append(content)

    for etc in etcs:
        content = {
                "title": (etc['이름']),
                "category": str(etc['구분']),
                "mapx":str(etc['xmap']),
                "mapy":str(etc['ymap']),
            }
        etcdict.append(content)


    API_KEY = getattr(settings, 'API_KEY', 'API_KEY')
    parkJson = json.dumps(parkdict, ensure_ascii=False)
    cafeJson = json.dumps(cafedict, ensure_ascii=False)
    bistroJson = json.dumps(bistrodict, ensure_ascii=False)
    etcJson = json.dumps(etcdict, ensure_ascii=False)

    placedict=[]
    places = placeAddByUser.objects.all()
    for place in places:
        content= {
            "title":place.name,
            "mapx":str(place.xmap),
            "mapy":str(place.ymap),
            "category":str(place.category),
            "author":str(place.created_by),
        }
        placedict.append(content)
    
    placeJson = json.dumps(placedict, ensure_ascii=False)
    user={'user':str(request.user)}
    userJson=json.dumps(user)

    return render(request, 'map/showmap.html', {'bistroJson':bistroJson, 'cafeJson':cafeJson, 'parkJson': parkJson, 'API_KEY' : API_KEY,'placeJson':placeJson,'userJson':userJson,'etcJson':etcJson,})

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
@login_required
def addplace(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        new_place=placeAddByUser()
        new_place.name=req['title']
        new_place.xmap=req['xmap']
        new_place.ymap=req['ymap']
        new_place.created_by=request.user
        new_place.category=req['category']
        new_place.save()
        return JsonResponse({'id': str(new_place.id)})
    elif request.method == 'GET':
        return render(request, 'base.html')

@csrf_exempt
@login_required
def addplacebysearch(request, searchword):
    if request.method == 'POST':
        req = json.loads(request.body)
        new_place=placeAddByUser()
        new_place.name=req['title']
        new_place.xmap=req['xmap']
        new_place.ymap=req['ymap']
        new_place.created_by=request.user
        new_place.category=req['category']
        new_place.save()
        return JsonResponse({'id': str(new_place.id)})
    elif request.method == 'GET':
        return render(request, 'base.html')


@csrf_exempt
@login_required
def deleteplace(request):
    if request.method=='POST':
       req = json.loads(request.body)
       title=req['title']
       place=placeAddByUser.objects.filter(name=title).first()
       if request.user==place.created_by:
           place.delete()
           type = "correct"
           return JsonResponse({'type': str(type)})
       else:
           type = "incorrect"
           return JsonResponse({'type': str(type)})
    
    elif request.method == 'GET':
        return render(request, 'base.html')


@csrf_exempt
@login_required
def deleteplacebysearch(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        title = req['title']
        place = placeAddByUser.objects.filter(name=title).first()
        if request.user == place.created_by:
            place.delete()
            type = "correct"
            return JsonResponse({'type': str(type)})
        else:
            type = "incorrect"
            return JsonResponse({'type': str(type)})

    elif request.method == 'GET':
        return render(request, 'base.html')


def search(request, searchword):
    with open('map/static/map/etc.json', encoding='utf-8') as json_file:
        etcs = json.load(json_file)

    with open('map/static/map/data.json', encoding='utf-8') as json_file:
        datas = json.load(json_file)

    parkdict = []
    cafedict = []
    bistrodict = []
    etcdict = []

    for data in datas:
        if data['종류'] == "식당":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category": str(data['종류']),
            }
            bistrodict.append(content)
        if data['종류'] == "카페":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category": str(data['종류']),
            }
            cafedict.append(content)
        if data['종류'] == "공원":
            content = {
                "title": (data['이름']),
                "address": str(data['주소']),
                "category": str(data['종류']),
            }
            parkdict.append(content)

    for etc in etcs:
        content = {
            "title": (etc['이름']),
            "category": str(etc['구분']),
            "mapx": str(etc['xmap']),
            "mapy": str(etc['ymap']),
        }
        etcdict.append(content)

    API_KEY = getattr(settings, 'API_KEY', 'API_KEY')
    parkJson = json.dumps(parkdict, ensure_ascii=False)
    cafeJson = json.dumps(cafedict, ensure_ascii=False)
    bistroJson = json.dumps(bistrodict, ensure_ascii=False)
    etcJson = json.dumps(etcdict, ensure_ascii=False)

    placedict = []
    places = placeAddByUser.objects.all()
    for place in places:
        content = {
            "title": place.name,
            "mapx": str(place.xmap),
            "mapy": str(place.ymap),
            "category": str(place.category),
            "author": str(place.created_by),
        }
        placedict.append(content)

    placeJson = json.dumps(placedict, ensure_ascii=False)
    user = {'user': str(request.user)}
    userJson = json.dumps(user)

    return render(request, 'map/showmap.html',
                  {'bistroJson': bistroJson, 'cafeJson': cafeJson, 'parkJson': parkJson, 'API_KEY': API_KEY,
                   'placeJson': placeJson, 'userJson': userJson, 'etcJson': etcJson, 'searchword':searchword})



