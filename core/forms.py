from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': "Ваше ім'я", 'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input', 'placeholder': 'you@example.com', 'autocomplete': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': '+380 XX XXX XX XX', 'autocomplete': 'tel',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': 'Тема звернення',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input form-textarea', 'placeholder': 'Ваше повідомлення', 'rows': 5,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 2:
            raise forms.ValidationError("Ім'я має містити щонайменше 2 символи.")
        return name

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        if len(message) < 10:
            raise forms.ValidationError('Повідомлення занадто коротке. Опишіть, будь ласка, детальніше.')
        return message
