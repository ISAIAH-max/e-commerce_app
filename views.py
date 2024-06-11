from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index_view(request):
    template = loader.get_template('master1.html')
    return HttpResponse(template.render())

def services_view(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def products_view(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())

def about_us_view(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())
    
def contact_us_view(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())

def projects_view(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())