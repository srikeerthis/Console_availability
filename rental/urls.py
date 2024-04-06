from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.view_consoles,name='view_consoles'),
    path('toggle/<int:console_id>/',views.toggle_rental_status,name='toggle_rental_status'),
    path('add_console/',views.add_console,name='add_console'),
    path('console_list/',views.console_list, name='console_list'),
    path('admin_login/',auth_views.LoginView.as_view(template_name='rental/admin_login.html'),name='admin_login')
]