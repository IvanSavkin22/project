from django import forms
from .models import Appointment, PersonalizationRequest


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['device_name', 'problem_description', 'phone_number']
        widgets = {
            'device_name': forms.TextInput(attrs={'placeholder': 'Компьютер или Ноутбук'}),
            'problem_description': forms.Textarea(attrs={'placeholder': 'Описание проблемы'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
        }
        labels = {
            'device_name': 'Название устройтва',
            'problem_description': 'Описание проблемы',
            'phone_number': 'Номер телефона',
        }



class PersonalizationForm(forms.ModelForm):
    class Meta:
        model = PersonalizationRequest
        fields = ['name', 'phone_number', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'description': forms.Textarea(attrs={'placeholder': 'Что вы хотите сделать?'}),
        }
        labels = {
            'name': 'Имя',
            'phone_number': 'Номер телефона',
            'description': 'Описание',
        }
