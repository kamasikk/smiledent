from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'phone', 'doctor', 'service',
        'preferred_date', 'preferred_time', 'status', 'created_at',
    )
    list_editable = ('status',)
    list_filter = ('status', 'doctor', 'service', 'preferred_date')
    search_fields = ('full_name', 'phone', 'email')
    date_hierarchy = 'preferred_date'
    autocomplete_fields = []
    fieldsets = (
        ('Пацієнт', {
            'fields': ('full_name', 'phone', 'email')
        }),
        ('Запис', {
            'fields': ('doctor', 'service', 'preferred_date', 'preferred_time', 'message')
        }),
        ('Обробка заявки', {
            'fields': ('status',)
        }),
    )
