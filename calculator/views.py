from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method =="POST":
        bcs = int(request.POST['level']) # 사진 선택한 값 가져오기.
        dog_breed = request.POST.get("dog_breed") # 종 선택 값 가져오기
        current_weight = int(request.POST['current_weight']) # 체중 가져오기
        appropriate_weight = int(current_weight)*(100-bcs)/100/0.8
        base_metabolism = 70*current_weight**0.75
        
        from .utils import to_calculate_result
        press_text, press_graph = to_calculate_result(dog_breed)
        
        ctx={
            'dog_breed':dog_breed, 
            'appropriate_weight':appropriate_weight, 
            'base_metabolism':base_metabolism,
            'press_text':press_text,
            'press_graph':press_graph,
            }

        return render(request, 'calculator/calculate_result.html', ctx)
    else:
        from .utils import return_dognames_list
        dognames_list = return_dognames_list()
        ctx={'breeds':dognames_list} # 데이터에 담겨 있어야 한다.
        return render(request, 'calculator/calculate.html', ctx) 