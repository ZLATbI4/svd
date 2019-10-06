from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    path('', views.items, name='items'),
    path('', views.products, name='portfolio'),
    path('', views.contact, name='contact'),
]
