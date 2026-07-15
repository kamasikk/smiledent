from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'rating', 'short_text', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'rating')
    search_fields = ('author_name', 'text')
    date_hierarchy = 'created_at'
    actions = ['approve_reviews']

    @admin.display(description='Текст')
    def short_text(self, obj):
        return obj.text[:60] + ('…' if len(obj.text) > 60 else '')

    @admin.action(description='Схвалити вибрані відгуки')
    def approve_reviews(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'Схвалено відгуків: {updated}')
