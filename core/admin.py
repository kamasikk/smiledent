from django.contrib import admin

from .models import FAQ, ContactMessage, Advantage


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    search_fields = ('question', 'answer')
    list_filter = ('is_published',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    list_editable = ('is_read',)
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
