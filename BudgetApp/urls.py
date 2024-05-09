from django.urls import path
from . import views

urlpatterns = [
    path('BudgetApp/', views.BudgetApp, name='BudgetApp'),
]