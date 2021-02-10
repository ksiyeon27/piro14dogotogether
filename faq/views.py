from django.shortcuts import render
from .models import Qna

# Create your views here.
def faq(request):
    qnas = Qna.objects.all() #모델 사용.
    ctx = {'qnas':qnas}
    return render(request, 'faq/qna.html', ctx)