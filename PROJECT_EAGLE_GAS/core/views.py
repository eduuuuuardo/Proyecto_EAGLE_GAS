from django.shortcuts import render

def home(request):
    """Renderiza la página de inicio."""
    return render(request, 'core/home.html')

def about(request):
    """Renderiza la página de 'Quiénes Somos'."""
    return render(request, 'core/about.html')

def products(request):
    """Renderiza la página de 'Productos'."""
    return render(request, 'core/products.html')

def services(request):
    """Renderiza la página de 'Servicios'."""
    return render(request, 'core/services.html')

def contact(request):
    """Renderiza la página de 'Contacto'."""
    return render(request, 'core/contact.html')

def login(request):
    """Renderiza la página de 'Iniciar Sesión'."""
    return render(request, 'core/login.html')

def create_invoice(request):
    """Renderiza la página para crear una factura."""
    return render(request, 'core/create_invoice.html')

# Renderiza la página del panel de usuario
def panel_usuario(request):
    """Renderiza el panel de usuario."""
    return render(request, 'core/panel_usuario.html')

# Renderiza la página de registro
def registro(request):
    """Renderiza la página de 'Regístrate aquí'."""
    return render(request, 'core/Regístrate aquí.html')