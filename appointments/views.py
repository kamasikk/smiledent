from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AppointmentForm


class BookingView(CreateView):
    form_class = AppointmentForm
    template_name = 'appointments/booking.html'
    success_url = reverse_lazy('appointments:success')

    def get_initial(self):
        initial = super().get_initial()
        service_slug = self.request.GET.get('service')
        doctor_slug = self.request.GET.get('doctor')
        if service_slug:
            from services.models import Service
            service = Service.objects.filter(slug=service_slug, is_active=True).first()
            if service:
                initial['service'] = service.pk
        if doctor_slug:
            from doctors.models import Doctor
            doctor = Doctor.objects.filter(slug=doctor_slug, is_active=True).first()
            if doctor:
                initial['doctor'] = doctor.pk
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Онлайн-запис до лікаря — SmileDent',
            'meta_description': (
                'Запишіться на прийом до стоматолога SmileDent онлайн за кілька хвилин. '
                'Оберіть зручну дату, час, лікаря та послугу.'
            ),
        })
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Вашу заявку прийнято! Ми зателефонуємо вам для підтвердження запису найближчим часом.'
        )
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Будь ласка, перевірте правильність заповнення форми.')
        return super().form_invalid(form)
