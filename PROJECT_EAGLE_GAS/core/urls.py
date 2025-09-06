from django.urls import path
from . import views

urlpatterns = [
    # Rutas principales del sitio web
    path('', views.home, name='home'),
    path('quienes-somos/', views.about, name='about'),
    path('productos/', views.products, name='products'),
    path('servicios/', views.services, name='services'),
    path('contacto/', views.contact, name='contact'),
    path('iniciar-sesion/', views.login, name='login'),
    # Ruta para la página de creación de facturas
    path('crear-factura/', views.create_invoice, name='create_invoice'),
]
