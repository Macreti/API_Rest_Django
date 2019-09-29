from django.urls import path
from . import views

app_name = 'use_api'

urlpatterns = [
    path('', views.PersonneAPIView.as_view(), name='recap_all'),
]