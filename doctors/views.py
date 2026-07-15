from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from services.models import Service

from .models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        return Doctor.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Наші лікарі — SmileDent',
            'meta_description': (
                'Команда досвідчених стоматологів SmileDent: терапевти, ортодонти, хірурги '
                'та імплантологи з багаторічним досвідом і сучасною кваліфікацією.'
            ),
        })
        return context


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/detail.html'
    context_object_name = 'doctor'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Doctor.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = self.object
        context.update({
            'meta_title': f'{doctor.full_name} — {doctor.specialty} | SmileDent',
            'meta_description': doctor.bio[:155],
            'services': Service.objects.filter(is_active=True)[:4],
        })
        return context
