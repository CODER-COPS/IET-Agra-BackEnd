from django.urls import path
from carousel import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.carousel_list),
    path('<int:pk>/', views.carousel_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
