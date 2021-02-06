from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method =="POST":
        bcs = int(request.POST['level']) # 사진 선택한 값 가져오기.
        dog_breed = request.POST.get("dog_breed") # 종 선택 값 가져오기
        current_weight = request.POST['current_weight'] # 체중 가져오기
        appropriate_weight = current_weight*(100-bcs)/100/0.8
        base_metabolism = 70*current_weight^0.75
        # 시연 크롤링
        response = requests.get(f"http://www.akc.org/dog-breeds/{dog_breed}/")
        from bs4 import BeautifulSoup as bs
        soup = bs(response.text, "html.parser")
        press_text = soup.select("#panel-EXERCISE p")[0]
        press_graph = soup.select('#panel-EXERCISE div.graph-section .bar-graph__section')[0].get('style')
        ctx={
            'dog_breed':dog_breed, 
            'appropriate_weight':appropriate_weight, 
            'base_metabolism':base_metabolism,
            'press_text':press_text,
            'press_graph':press_graph,
            }
        return render(request, 'dog/calculate_result.html', ctx)
    else:
        breeds = []
        ctx={'breeds':breeds} # 데이터에 담겨 있어야 한다.
        return render(request, 'dog/calculate.html', ctx)