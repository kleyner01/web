from django.urls import path
from . import views

urlpatterns = [
    path('trabalhe_conoscos/', views.CandidatoViews, name='trabalhe_conoscos'),
]
