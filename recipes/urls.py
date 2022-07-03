from recipes import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),

]