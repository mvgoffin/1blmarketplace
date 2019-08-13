"""thecheckout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from profiles import views
from checkout import views as checkout_views
from users import views as user_views

#from thecheckout.views import home, send_push #web-push

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calm_bottle/', user_views.calm_bottle, name='calm-bottle'),
    path('skincare_bottle/', user_views.skincare_bottle, name='skincare-bottle'),
    path('register_calm_bottle/', user_views.register_calm_bottle, name='register_calm_bottle'),
    path('register_skincare_bottle/', user_views.register_skincare_bottle, name='register_skincare_bottle'),
    #path('register_box/', user_views.register_box, name='register_box'),
    #path('register_mx/', user_views.register_mx, name='register_mx'),
    #path('register_le/', user_views.register_le, name='register_le'),
    #path('register_hc/', user_views.register_hc, name='register_hc'),
    #path('access_code/', user_views.access_code, name='access_code'),
    path('checkout_bottle/', checkout_views.checkout_bottle, name='checkout_bottle'),
    path('checkout_box/', checkout_views.checkout_box, name='checkout_box'),
    path('checkout_sca/', checkout_views.checkout_sca, name='checkout_sca'),
    #path('checkout_box/', checkout_views.checkout_box, name='checkout_box'),
    #path('checkout_mx/', checkout_views.checkout_mx, name='checkout_mx'),
    #path('checkout_le/', checkout_views.checkout_le, name='checkout_le'),
    #path('checkout_hc/', checkout_views.checkout_hc, name='checkout_hc'),
    path('terms-of-service/', views.termsofservice, name='terms-of-service'),
    path('privacy-policy/', views.privacypolicy, name='privacy-policy'),
    path('sms-policy/', views.smspolicy, name='sms-policy'),
    path('success/', views.success, name='success'),
    path('hometest/', views.hometest, name='hometest'),
    #path('code_granted/', views.code_granted, name='code_granted'),
    
    

#web-push
    #path('', home),
    #path('send_push', send_push),
    #path('webpush/', include('webpush.urls')),
]
