from django.contrib import admin

from .models import ServiceCategory, Service


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_from', 'duration_minutes', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'short_description', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'slug', 'category', 'icon', 'image')
        }),
        ('Опис', {
            'fields': ('short_description', 'description')
        }),
        ('Вартість і тривалість', {
            'fields': ('price_from', 'duration_minutes')
        }),
        ('Публікація', {
            'fields': ('order', 'is_active')
        }),
    )
