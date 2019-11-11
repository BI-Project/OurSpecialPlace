from django.contrib import admin
from django.urls import path, include
from .views import QuestionFormTemplateView

app_name = 'recommendation'

urlpatterns = [
    path('', QuestionFormTemplateView.as_view(), name='question_form')
]
