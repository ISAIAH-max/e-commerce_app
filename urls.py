from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home_page'),
    path('Home', views.index_view, name='home_page'),
    path('Contacts Us', views.contact_us_view, name='contact_us'),
    path('Products', views.products_view, name='products'),
    path('Services', views.services_view, name='services'),
    path('Projects', views.projects_view, name='projects'),
    path('About Us', views.about_us_view, name='about'),
]
