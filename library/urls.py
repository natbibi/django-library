from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('bookshelf.urls')),
    path('admin/', admin.site.urls),
    path('signup/', user_views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
