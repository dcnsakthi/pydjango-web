"""
Definition of urls for pydjango_web.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

admin.site.site_header = 'dcnsakthi.co Admin'         # default: "Django Administration"
admin.site.index_title = 'dcnsakthi.co Admin'    # default: "Site administration"
admin.site.site_title = 'dcnsakthi.co Admin'                   # default: "Django site admin"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('admin/', views.admin, name='admin'),
]
