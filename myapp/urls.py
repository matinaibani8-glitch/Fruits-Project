from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home),
    path("login/",views.login,name="login"),
    path("index/",views.index,name="index"),
    path("updateprofile/",views.updateprofile,name="updateprofile"),
    path("userlogout/",views.userlogout,name="logout"),
    path("about/",views.about,name="about"),
    path("service/",views.service,name="service"),
    path("blog/",views.blog,name="blog"),
    path("feature/",views.feature,name="feature"),
    path("team/",views.team,name="team"),
    path("testimonial/",views.testimonial,name="testimonial"),
    path("404/",views.error,name="error"),
    path("contact/",views.contact,name="contact"),
]