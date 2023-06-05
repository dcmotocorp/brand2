# myapp/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register(r'startups',views.Startups
)
route.register(r'investors',views.InvestorsList
)
route.register(r'audiences',views.AudienceListList
)



urlpatterns = [
] + route.urls
