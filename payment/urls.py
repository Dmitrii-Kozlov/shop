from django.urls import path

from  . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.patment_done, name='done'),
    path('canceled/', views.patment_canceled, name='canceled'),
]