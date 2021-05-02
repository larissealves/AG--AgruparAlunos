from django.urls import path
from . import views

urlpatterns = [ 
   path('', views.resultados, name='resultados'),
]
