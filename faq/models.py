from django.db import models

class Qna(models.Model):
    question = models.TextField(default=None, verbose_name='질문')
    answer = models.TextField(default=None, verbose_name='답변')

