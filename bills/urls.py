from django.urls import path
from . import views

app_name = 'bills'

urlpatterns = [
    path('bill/', views.PersonneListCreate.as_view(), name='create'),
]