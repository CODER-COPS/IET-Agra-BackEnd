from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),

    path('carousel/', include('api.carousel.urls')),
    path('notification/', include('api.notification.urls')),
    path('event/', include('api.event.urls')),

]
