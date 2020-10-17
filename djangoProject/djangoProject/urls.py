"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from users.views import register_view, profile_view
from django.contrib.auth import views as auth_views
from houses.views import house_view,add_house_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('register/',register_view, name='register-view'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login-view'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout-view'),
    path('profile/',profile_view, name = 'profile-view'),
    path('view-house/',house_view,name = 'house-view'),
    path('add-house/',add_house_view, name = 'add-house-view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
