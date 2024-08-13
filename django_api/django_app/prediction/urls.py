# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# prediction/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('predictions/', views.prediction_list, name='prediction_list'),
]
