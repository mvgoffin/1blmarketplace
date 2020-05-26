from django.shortcuts import render
from django.shortcuts import redirect

#from profiles.forms import Access (diabling PLNT PROTEIN IG landing page)
#from profiles.forms import AccessForm (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import EmailMessage (diabling PLNT PROTEIN IG landing page)
#from django.core.mail import send_mail (diabling PLNT PROTEIN IG landing page)
from django.conf import settings

# Create your views here.

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

#1BLives - Rockstar
def rockstar_home(request):
    context = locals()
    template = 'rockstar_home.html'
    return render(request,template,context)

def rockstar_about(request):
    context = locals()
    template = 'rockstar_about.html'
    return render(request,template,context)

def rockstar_registration(request):
    context = locals()
    template = 'rockstar_registration.html'
    return render(request,template,context)

def rockstar_laptops(request):
    context = locals()
    template = 'rockstar_laptops.html'
    return render(request,template,context)
    
def rockstar_product(request):
    context = locals()
    template = 'rockstar_product.html'
    return render(request,template,context)

def rockstar_checkout(request):
    context = locals()
    template = 'rockstar_checkout.html'
    return render(request,template,context)

def rockstar_thankyou(request):
    context = locals()
    template = 'rockstar_thankyou.html'
    return render(request,template,context)


#greencourt technologies
def gclogin(request):
    context = locals()
    template = 'gclogin.html'
    return render(request,template,context)

def gcpage(request):
    context = locals()
    template = 'gcpage.html'
    return render(request,template,context)
