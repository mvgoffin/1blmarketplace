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

#1BLives - Zoi
def zoi_home(request):
    context = locals()
    template = 'zoi_home.html'
    return render(request,template,context)

def zoi_about(request):
    context = locals()
    template = 'zoi_about.html'
    return render(request,template,context)

def zoi_registration(request):
    context = locals()
    template = 'zoi_registration.html'
    return render(request,template,context)

def zoi_laptops(request):
    context = locals()
    template = 'zoi_laptops.html'
    return render(request,template,context)
    
def zoi_product(request):
    context = locals()
    template = 'zoi_product.html'
    return render(request,template,context)

def zoi_checkout(request):
    context = locals()
    template = 'zoi_checkout.html'
    return render(request,template,context)

def zoi_thankyou(request):
    context = locals()
    template = 'zoi_thankyou.html'
    return render(request,template,context)


