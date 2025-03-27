from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('cesium/', views.cesium_data_view, name='cesium_data'),
    
    # Using django-allauth's login view (or you can use the default Django login view)
    path('login/', views.login_view, name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Ensure redirect after logout
    
    # You can keep this as your custom signup view or use django-allauth's signup view.
    path('signup/', views.signup, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
