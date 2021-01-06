from django.urls import path
from django.utils.translation import gettext_lazy as _
from  . import views

app_name = 'payment'

urlpatterns = [
    path(_('process/'), views.payment_process, name='process'),
    path(_('done/'), views.patment_done, name='done'),
    path(_('canceled/'), views.patment_canceled, name='canceled'),
]