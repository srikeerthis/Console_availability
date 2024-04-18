from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.view_consoles,name='view_consoles'),
    # path('toggle/<int:console_id>/',views.toggle_rental_status,name='toggle_rental_status'),
    path('add_console/',views.add_console,name='add_console'),
    path('console_list/',views.console_list, name='console_list'),
    path('admin_login/',auth_views.LoginView.as_view(template_name='rental/admin_login.html'),name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('edit_console/<int:console_id>',views.edit_consoles,name='edit_console'),
    path('delete_console/<int:console_id>',views.delet_console,name='delete_console'),
    # path('toggle-repair/<int:console_id>/', views.toggle_repair_status, name='toggle_repair_status'),

]