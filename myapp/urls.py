from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event1/', views.event1, name='event1'),
    path('event2/', views.event2, name='event2'),
    path('event3/', views.event3, name='event3'),
    path('event4/', views.event4, name='event4'),
    path('register/', views.student_register, name='register'),
    path('success/' , views.success , name="success")
]
