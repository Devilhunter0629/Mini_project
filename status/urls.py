from django.urls import path, include
from . import views

urlpatterns = [
    path('all-status/', views.statuses, name='statuses'),
]


