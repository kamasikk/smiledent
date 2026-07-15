from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from smiledent.sitemaps import sitemaps

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('doctors/', include('doctors.urls')),
    path('services/', include('services.urls')),
    path('reviews/', include('reviews.urls')),
    path('booking/', include('appointments.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
