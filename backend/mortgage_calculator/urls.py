from django.urls import path

from .views import MortgageListCreate

urlpatterns = [path("", MortgageListCreate.as_view(), name="list_mortgage_records")]
