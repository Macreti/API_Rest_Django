from django.shortcuts import render
from bills.models import Personne
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class PersonneAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'use_api/index.html'

    def get(self, request):
        queryset = Personne.objects.all()
        return Response ({'recap': queryset})


