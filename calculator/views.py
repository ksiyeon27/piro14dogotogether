
from django.shortcuts import render
from .forms import CalculatorForm
from .utils import to_calculate_result, calculate_weight_status, return_dogkrname 


def firstpage(request):
    return render(request, 'calculator/firstpage.html')


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            bcs = int(form.cleaned_data['bcs'])
            dog_breed = form.cleaned_data['breeds']
            current_weight =int(form.cleaned_data['current_weight'])
            appropriate_weight = round(current_weight*(100-bcs)/100*1.25, 3)
            base_metabolism = round(70*current_weight**0.75, 3)
            weight_status1 = calculate_weight_status(current_weight, appropriate_weight)
            weight_status2 = calculate_weight_status(appropriate_weight, current_weight)

            # 크롤링 한 문단과 그래프 css style 가져오기
            press_text, press_graph, press_image = to_calculate_result(dog_breed)

            # 강아지 한글 이름을 template으로 넘겨주기 위해 딕셔너리로 key, value 전환
            dogkrname_list = return_dogkrname()
            dogkrname_dict = {key:value for key, value in dogkrname_list}
            dogkrname = dogkrname_dict[dog_breed]

            ctx={
                'dog_breed':dogkrname, 
                'current_weight':current_weight,
                'appropriate_weight':appropriate_weight, 
                'base_metabolism':base_metabolism,
                'weight_status1':weight_status1,
                'weight_status2':weight_status2,
                'press_text':press_text,
                'press_graph':press_graph,
                'press_image':press_image,
                }

            return render(request, 'calculator/calculate_result.html', ctx)
        else:
            return render(request, 'calculator/calculate.html', {'form':form})
    else:
        form = CalculatorForm()
        ctx = {'form':form}
        return render(request, 'calculator/calculate.html', ctx) 

