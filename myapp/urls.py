from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event1/', views.event1, name='event1'),
    path('event2/', views.event2, name='event2'),
    path('event3/', views.event3, name='event3'),
    path('event4/', views.event4, name='event4'),
    path('event5/', views.event5, name='event5'),
    path('event6/', views.event6, name='event6'),
    path('event7/', views.event7, name='event7'),
    path('event8/', views.event8, name='event8'),
    path('event9/', views.event9, name='event9'),
    path('event10/', views.event10, name='event10'),
    path('event11/', views.event11, name='event11'),
    path('event12/', views.event12, name='event12'),
    path('event13/', views.event13, name='event13'),
    path('register/', views.student_register, name='register'),
    path('success/' , views.success , name="success"),
    path('view-draws/', views.view_draws, name='view_draws'),
]
