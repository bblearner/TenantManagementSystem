
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from users.views import register_view, profile_view, delete_user
from django.contrib.auth import views as auth_views
from houses.views import house_view,add_house_view,house_info,update_house, rent_house, delete_house

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('register/',register_view, name='register-view'),
    path('delete/',delete_user, name = 'delete-view'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login-view'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout-view'),
    path('delete/',delete_user, name = 'delete-view'),
    path('profile/',profile_view, name = 'profile-view'),
    path('view-house/',house_view,name = 'house-view'),
    path('add-house/',add_house_view, name = 'add-house-view'),
    path('view-house/<single_slug>/', house_info, name = 'house-info'),
    path('search/<single_slug>/', house_info),
    path('view-house/<single_slug>/update_house/', update_house, name='update-house'),
    path('search/<single_slug>/update_house/', update_house),
    path('search/<single_slug>/rent_house/', rent_house, name='rent-house'),
    path('view-house/<single_slug>/delete_house/',delete_house,name = 'delete-house-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
