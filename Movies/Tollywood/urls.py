from django.urls import path,include
from Tollywood import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('data/',views.data,name="data"),
    path('edit/<str:id>/',views.edit,name="edit"),
    path('update/<str:id>/',views.update,name="update"),
    path('userregister/',views.userregister,name="userregister"),
    path('userdata/',views.userdata,name="userdata"),
    path('uedit/<str:id>/',views.uedit,name="uedit"),
    path('udelete/<str:id>/',views.udelete,name="udelete"),
]