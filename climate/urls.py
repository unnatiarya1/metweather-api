# climate/urls.py

from django.urls import path
from .views import ClimateDataListView

urlpatterns = [
    path('climate/', ClimateDataListView.as_view(), name='climate-data'),
]
