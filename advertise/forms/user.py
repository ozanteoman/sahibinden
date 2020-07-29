from django import forms

from advertise.choices import GenderChoices
from advertise.models import User


class UpdateUserForm(forms.ModelForm):
    birthday = forms.DateTimeField(
        label="Doğum Tarihi",
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'data-target': '#id_birthday',
            'data-toggle': "datetimepicker",
        })
    )

    gender = forms.ChoiceField(label="Cinsiyet", choices=GenderChoices.CHOICES, widget=forms.RadioSelect, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'gender',
                  'marital_status', 'educational_status', 'profession',
                  'interests', 'phone_number']

        widgets = {
            'interests': forms.CheckboxSelectMultiple,
        }

        labels = {
            'marital_status': "Medeni Hali",
            'educational_status': "Eğitim Durumu",
            'profession': "Meslek",
            'interests': "İlgi Alanları",
            'phone_number': "Telefon Numarası",
        }
