from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
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
    parkJson = json.dumps(parkdict, ensure_ascii=False)
    return render(request, 'map/showmap.html', {'parkJson': parkJson})

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