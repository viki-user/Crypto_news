from django.urls import path
from .views import home,timeline,faq,about,economic,IIpay




urlpatterns = [
    path('',home,name="home"),
    path('timeline',timeline,name="timeline",),
    path('faq',faq,name="faq",),
    path('about',about,name="about",),
    path('economic',economic,name="economic",),
    path('IIpay',IIpay,name="IIpay",),

]