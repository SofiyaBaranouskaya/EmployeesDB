from django.urls import path
from . import views
from .views import employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
]
