from datetime import date, time, timedelta

from django import forms

from doctors.models import Doctor
from services.models import Service

from .models import Appointment

CLINIC_OPEN_TIME = time(9, 0)
CLINIC_CLOSE_TIME = time(19, 0)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name', 'phone', 'email', 'doctor', 'service',
            'preferred_date', 'preferred_time', 'message',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': "Ваше ім'я та прізвище", 'autocomplete': 'name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': '+380 XX XXX XX XX', 'autocomplete': 'tel',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input', 'placeholder': 'you@example.com (необов\'язково)', 'autocomplete': 'email',
            }),
            'doctor': forms.Select(attrs={'class': 'form-input'}),
            'service': forms.Select(attrs={'class': 'form-input'}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'message': forms.Textarea(attrs={
                'class': 'form-input form-textarea', 'rows': 4,
                'placeholder': 'Додаткова інформація (необов\'язково)',
            }),
        }
        labels = {
            'doctor': 'Бажаний лікар',
            'service': 'Послуга',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.filter(is_active=True)
        self.fields['doctor'].required = False
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['service'].required = False
        self.fields['email'].required = False

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()
        if len(full_name) < 3:
            raise forms.ValidationError("Вкажіть, будь ласка, повне ім'я.")
        return full_name

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data['preferred_date']
        if preferred_date < date.today():
            raise forms.ValidationError('Дата запису не може бути в минулому.')
        if preferred_date > date.today() + timedelta(days=90):
            raise forms.ValidationError('Запис можливий не більше ніж на 90 днів наперед.')
        return preferred_date

    def clean_preferred_time(self):
        preferred_time = self.cleaned_data['preferred_time']
        if preferred_time < CLINIC_OPEN_TIME or preferred_time > CLINIC_CLOSE_TIME:
            raise forms.ValidationError('Клініка працює з 09:00 до 19:00. Оберіть інший час.')
        return preferred_time

    def clean(self):
        cleaned_data = super().clean()
        preferred_date = cleaned_data.get('preferred_date')
        preferred_time = cleaned_data.get('preferred_time')
        if preferred_date == date.today() and preferred_time:
            from datetime import datetime
            now = datetime.now().time()
            if preferred_time <= now:
                raise forms.ValidationError('Оберіть, будь ласка, час у майбутньому.')
        return cleaned_data
