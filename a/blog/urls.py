from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.map, name='map'),
    path('booking/', views.booking, name='booking'),
    path('thanks/', views.thanks, name='thanks'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
