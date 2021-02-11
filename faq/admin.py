from django.contrib import admin
from faq.models import Qna

@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

