from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='list'),
    path('prices/', views.PriceListView.as_view(), name='prices'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='detail'),
]
