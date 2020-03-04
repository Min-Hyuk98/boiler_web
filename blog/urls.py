"""emocon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('', first, name='service'),
    path('index', index, name='index'),
    path('service/', service, name='service'),
    path('service_popup/', service_popup, name='service_popup'),
    path('service_boiler/', service_boiler, name='service_boiler'),
    path('service_onsugi/', service_onsugi, name='service_onsugi'),
    path('service_aircon/', service_aircon, name='service_aircon'),
    path('daesung_info/', daesung_info, name='daesung_info'),
    path('navien_info/', navien_info, name='navien_info'),
    path('kiturami_info/', kiturami_info, name='kiturami_info'),
    path('rinnai_info/', rinnai_info, name='rinnai_info'),

    path('product_info/', product_info, name='product_info'),
    path('consult/', consult, name='consult'),
    path('consult_content/', consult_content, name='consult_content'),
    path('recent/', recent, name='recent'),
    path('customer/', customer, name='customer'),
    path('map/', map_1, name='map')

]
