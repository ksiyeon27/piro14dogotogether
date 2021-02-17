from django.shortcuts import render
import json

# Create your views here.
def faq(request):



    with open('./faq/static/faq/js/qnas.json', encoding='utf-8') as json_file:
        qnas = json.load(json_file)
        qnalist = []
        for qna in qnas:
            if qna.get('q'):
                item=[str(qna['q']),str(qna['a'])]

                qnalist.append(item)

    return render(request, 'faq/qna.html', {'qnalist':qnalist})