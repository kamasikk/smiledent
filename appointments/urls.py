from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.BookingView.as_view(), name='booking'),
    path('success/', TemplateView.as_view(
        template_name='appointments/success.html',
        extra_context={
            'meta_title': 'Заявку надіслано — SmileDent',
            'meta_description': 'Дякуємо, вашу заявку на запис прийнято.',
        },
    ), name='success'),
]
