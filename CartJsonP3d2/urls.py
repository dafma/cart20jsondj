"""CartJsonP3d2 URL Configuration

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
from django.urls import path, re_path
from django.conf import settings
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('(bikes|books|music)/<slug:category>', category1, name="category"),
	#path(r'^(<string:category>(bikes|books|music))/(<int:p_id>\d{1,})-(.*)/$','app.views.product', name="product"),
    re_path(r'^(?P<category>(bikes|books|music))/(?P<p_id>\d{1,})-(.*)/$', product, name="product"),
	path('checkout/', checkOut, name="checkOut"),
	# path('^logout/', 'userprofiles.views.userLogOut', name="userLogOut"),
	path('search/', search),
	# path('^sign/', 'userprofiles.views.signDispatcher', name="sign"),
	# path('^login/', 'userprofiles.views.registrarme', name="registrarme"),
	# path('^upload/(<string:path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
]
