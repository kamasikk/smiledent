from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ReviewForm
from .models import Review


class ReviewListView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/list.html'
    success_url = reverse_lazy('reviews:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(is_approved=True)
        avg_rating = 0
        if reviews.exists():
            avg_rating = round(sum(r.rating for r in reviews) / reviews.count(), 1)
        context.update({
            'meta_title': 'Відгуки пацієнтів — SmileDent',
            'meta_description': (
                'Реальні відгуки пацієнтів клініки SmileDent про якість лікування, '
                'сервіс та ставлення лікарів.'
            ),
            'reviews': reviews,
            'avg_rating': avg_rating,
            'reviews_count': reviews.count(),
        })
        return context

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            'Дякуємо за ваш відгук! Він з\'явиться на сайті після модерації.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Будь ласка, виправте помилки у формі відгуку.')
        return self.render_to_response(self.get_context_data(form=form))
