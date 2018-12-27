"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.conf.urls import url,includde
from django.contrib import admin   #include is write important
from django.urls import path
from django.conf.urls import include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage_view),
    path('python', views.pythonexam_view),
    path('java', views.javaexam_view),
    path('aptitude', views.aptitudeexam_view),
    path('home', views.homepage_view),
    path('signup', views.signup_view),
    path('accounts/', include('django.contrib.auth.urls')),  #This line is very important for authanticate
    path('logout/', views.logout_view),
    path('company_detail', views.CompanyListView.as_view(),name='companies'),
    path('<int:pk>', views.CompanyDetailView.as_view(),name='detail'),
    path('create', views.CompanyCreateView.as_view()),
    path('update/<int:pk>', views.CompanyUpdateView.as_view()),
    path('delete/<int:pk>', views.CompanyDeleteView.as_view()),
 #This line is very important for authanticate
]
