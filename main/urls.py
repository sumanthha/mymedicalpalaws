# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^login', views.LoginPageView.as_view()),
    url(r'^signup', views.SignUpPageView.as_view()),
]
