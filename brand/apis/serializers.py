from rest_framework import serializers
from .models import Startups, Investors, AudienceList, InvestorOfficesList, StartupsOfficesList


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startups
        fields = "__all__" 

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investors
        fields = "__all__"


class AudienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceList
        fields = "__all__"

class StartupsOfficesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupsOfficesList
        fields = "__all__"

class InvestorOfficesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorOfficesList
        fields = "__all__"