from django.contrib import admin
from django.urls import path
from . import views
# app_name = 'recipeshare'
urlpatterns = [
    path('',views.home,name='home' ),
    path('login/',views.login_,name='login' ),
    path('register-staff/',views.register_staff,name='register-staff' ),
    path('logout/',views.logout_,name='logout' ),
    path('admin-home/',views.admin_,name='admin-home' ),
    path('admin-home/<str:links>',views.links,name='links' ),
    path('staff-home/',views.staff_,name='staff-home' ),
    path('view-tables/',views.view_tables,name='view_tables' ),
    path('back-home/',views.back_home,name='back-home' ),   
    path('modify-tables/',views.modify_tables,name='modify-tables' ),
    path('modify-staff/',views.modify_staff,name='modify-staff' ),
    path('fetch_staff/',views.fetch_staff,name='fetch_staff' ),
    path('delete_staff/',views.delete_staff,name='delete_staff' ),
    path('view-staff/',views.view_staff,name='view-staff' ),
    path('fetch_tables/',views.fetch_tables,name='fetch_tables' ),
    path('delete_table/',views.delete_table,name='delete_table' ),
    path('add_table/<int:table_number>/',views.add_table,name='add_table' ),
    path('view-menu/',views.view_menu,name='view-menu' ),
    path('fetch_menu/',views.fetch_menu,name='fetch_menu' ),
    path('fetch_categories/',views.fetch_categories,name='fetch_categories' ),
    path('modify_menu/',views.modify_menu,name='modify_menu' ),
    path('add_item/<str:item>/<str:category>/<int:price>/',views.add_item,name='add_item' ),
    path('add_category/<str:category>/',views.add_category,name='add_category' ),
    path('delete_category/<int:id>/',views.delete_category,name='delete_category' ),
    path('delete_item/<int:id>/',views.delete_item,name='delete_item' ),
]