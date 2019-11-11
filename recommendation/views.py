from django.shortcuts import render
from django.views.generic import TemplateView


class QuestionFormTemplateView(TemplateView):
    template_name = 'recommendation/question_form.html'