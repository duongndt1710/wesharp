from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path('personal', views.personal_memo, name='personal_memo'),
]