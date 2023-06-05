from django.shortcuts import render
from .models import Startups, Investors, AudienceList, StartupsOfficesList, InvestorOfficesList
from .serializers import StartupSerializer,InvestorSerializer, AudienceListSerializer,StartupsOfficesListSerializer,InvestorOfficesListSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet



# Create your views here.

# =============== START UPS =========================



# @api_view(("GET",))
# def get_all_startups(request):
#     instants = Startups.objects.all()
#     serializers = StartupSerializer(instants,many=True)
#     return Response(serializers.data,status=status.HTTP_200_OK)


class Startups(ModelViewSet):
    queryset = Startups.objects.all()
    serializer_class = StartupSerializer
    

class InvestorsList(ModelViewSet):
    queryset = Investors.objects.all()
    serializer_class = InvestorSerializer

class AudienceListList(ModelViewSet):
    queryset = AudienceList.objects.all()
    serializer_class = AudienceListSerializer
 
class StartupsOfficesList(ModelViewSet):
    queryset = StartupsOfficesList.objects.all()
    serializer_class = StartupsOfficesListSerializer

class InvestorOfficesList(ModelViewSet):
    queryset = InvestorOfficesList.objects.all()
    serializer_class = InvestorOfficesListSerializer


