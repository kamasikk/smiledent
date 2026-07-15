from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'rating', 'text']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': "Ваше ім'я",
            }),
            'rating': forms.Select(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={
                'class': 'form-input form-textarea', 'placeholder': 'Розкажіть про свій досвід лікування', 'rows': 5,
            }),
        }

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if len(text) < 15:
            raise forms.ValidationError('Будь ласка, напишіть трохи докладніше про свій досвід (мінімум 15 символів).')
        return text
