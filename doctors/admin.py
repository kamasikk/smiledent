from django.contrib import admin
from django.utils.html import format_html

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'full_name', 'specialty', 'experience_years', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'specialty')
    search_fields = ('full_name', 'specialty', 'bio')
    prepopulated_fields = {'slug': ('full_name',)}
    fieldsets = (
        ('Основна інформація', {
            'fields': ('full_name', 'slug', 'specialty', 'photo', 'experience_years')
        }),
        ('Деталі', {
            'fields': ('education', 'bio')
        }),
        ('Публікація', {
            'fields': ('order', 'is_active')
        }),
    )

    @admin.display(description='Фото')
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:40px;width:40px;border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return '—'
