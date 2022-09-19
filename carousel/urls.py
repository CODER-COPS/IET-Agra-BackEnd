from django.urls import path
from carousel import views

urlpatterns = [
    path('', views.carousel_list),
    path('<int:pk>/', views.carousel_detail),
]
