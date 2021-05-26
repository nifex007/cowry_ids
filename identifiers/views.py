from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from identifiers.serializers import IdentifiersSerializer
from identifiers.models import Identifier
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse('<h1 style="text-align:center; font-size: 50px; margin-top: 25%">Cowry Identifiers</h1>')


class IdentifiersView(APIView):
    serializer_class = IdentifiersSerializer

    def get(self, request):
        new_identifier = Identifier()
        new_identifier.save()
        identifiers = Identifier.objects.all()
        serializer = self.serializer_class(identifiers)
        return Response(serializer.data, status=status.HTTP_200_OK)
