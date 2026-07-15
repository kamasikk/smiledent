from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from doctors.models import Doctor
from services.models import Service
from reviews.models import Review

from .forms import ContactForm
from .models import FAQ, Advantage


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'SmileDent — Стоматологічна клініка преміум-класу в Києві',
            'meta_description': (
                'SmileDent — сучасна стоматологія з європейськими стандартами лікування. '
                'Безболісне лікування, досвідчені лікарі, найновіше обладнання. Запишіться онлайн.'
            ),
            'doctors': Doctor.objects.filter(is_active=True)[:4],
            'services': Service.objects.filter(is_active=True).select_related('category')[:6],
            'reviews': Review.objects.filter(is_approved=True)[:6],
            'advantages': Advantage.objects.all()[:6],
            'faqs': FAQ.objects.filter(is_published=True)[:5],
        })
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Про клініку — SmileDent',
            'meta_description': (
                'Дізнайтеся більше про клініку SmileDent: наша місія, цінності, обладнання '
                'та підхід до лікування, орієнтований на комфорт пацієнта.'
            ),
            'advantages': Advantage.objects.all(),
            'doctors_count': Doctor.objects.filter(is_active=True).count(),
        })
        return context


class FAQView(TemplateView):
    template_name = 'core/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Часті запитання — SmileDent',
            'meta_description': 'Відповіді на найпопулярніші запитання пацієнтів клініки SmileDent.',
            'faqs': FAQ.objects.filter(is_published=True),
        })
        return context


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Контакти — SmileDent',
            'meta_description': "Адреса, телефон та форма зв'язку клініки SmileDent. Ми завжди раді відповісти на ваші запитання.",
        })
        return context

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Дякуємо! Ваше повідомлення надіслано. Ми зв'яжемося з вами найближчим часом."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Будь ласка, виправте помилки у формі нижче.')
        return super().form_invalid(form)


def error_404(request, exception=None):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
