from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from doctors.models import Doctor
from services.models import Service


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home', 'core:about', 'core:faq', 'core:contact',
            'services:list', 'services:prices', 'doctors:list',
            'reviews:list', 'appointments:booking',
        ]

    def location(self, item):
        return reverse(item)


class DoctorSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Doctor.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ServiceSitemap(Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    'static': StaticViewSitemap,
    'doctors': DoctorSitemap,
    'services': ServiceSitemap,
}
