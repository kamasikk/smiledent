from django.views.generic import ListView, DetailView

from .models import Service, ServiceCategory


class ServiceListView(ListView):
    model = Service
    template_name = 'services/list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Послуги — SmileDent',
            'meta_description': (
                'Повний перелік стоматологічних послуг клініки SmileDent: терапія, хірургія, '
                'ортодонтія, імплантація, відбілювання, дитяча стоматологія та профілактика.'
            ),
            'categories': ServiceCategory.objects.all(),
        })
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        context.update({
            'meta_title': f'{service.name} — SmileDent',
            'meta_description': service.short_description,
            'related_services': Service.objects.filter(
                is_active=True, category=service.category
            ).exclude(pk=service.pk)[:3],
        })
        return context


class PriceListView(ListView):
    model = Service
    template_name = 'services/prices.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta_title': 'Ціни на послуги — SmileDent',
            'meta_description': (
                'Прозорий прайс-лист клініки SmileDent. Дізнайтеся вартість консультації, '
                'лікування карієсу, імплантації, брекет-систем та інших послуг.'
            ),
            'categories': ServiceCategory.objects.prefetch_related('services'),
        })
        return context
