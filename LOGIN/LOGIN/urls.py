"""LOGIN URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from django.conf.urls import url

from .api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LOGIN/', include('django.contrib.auth.urls')),
    path('',views.Indexpage),
    path('Home',views.homepage, name="Home"),
    
    path('Registration', views.UserReg, name="Reg"),
    path('Login',views.loginpage, name="Loginpage"),
    path('Logout',views.logout, name="Logout"),
    path('View',views.view,name="View"),
    
    path('MainSharing',views.mainSharing, name="MainSharing"),
    path('Sharing',views.sharing, name="Sharing"),
    #path('ViewSharing',views.viewSharing,name="ViewSharing"),
    path('UpdateSharing',views.updateSharing, name="UpdateSharing"),
    path('DeleteSharing', views.deleteSharing, name="DeleteSharing"),

    path('MainGroup',views.mainGroup, name="MainGroup"),
    path('Group',views.group, name="Group"),
    path('MyGroup',views.myGroup, name="MyGroup"),

    path('MainMember', views.mainMember, name="MainMember"),
    path('Member',views.member, name="Member"),
    path('MyMember',views.myMember, name="MyMember"),

    path('Workshop',views.workshop, name="Workshop"),
    path('Booking',views.booking, name="Booking"),
    path('CreateWorkshop',views.createWorkshop, name="CreateWorkshop"),

    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<Person>\d+)/$', UserDetail.as_view(), name='user_list'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API') 
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







