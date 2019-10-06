from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('items.html', views.items, name='items'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('contact.html', views.contact, name='contact'),
]
