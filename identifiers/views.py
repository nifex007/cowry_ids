from django.shortcuts import render
from rest_framework.views import APIView
from identifiers.serializers import IdentifiersSerializer
from identifiers.models import Identifier
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class IdentifiersView(APIView):
    serializer_class = IdentifiersSerializer

    def get(self, request):
        new_identifier = Identifier()
        new_identifier.save()
        identifiers = Identifier.objects.all()
        serializer = self.serializer_class(identifiers)
        return Response(serializer.data, status=status.HTTP_200_OK)
