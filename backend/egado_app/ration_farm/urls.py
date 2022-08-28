from django.urls import path
from . import views

urlpatterns = [
    path('', views.RationFarmListAPIView.as_view(), name="ration_farm_list"),
    path('<int:id>', views.RationFarmDetailAPIView.as_view(), name="ration_farm_detail"),  
]