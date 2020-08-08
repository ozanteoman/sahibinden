import re
from datetime import datetime

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

    def clean_birthday(self):
        cleaned_data = self.cleaned_data.get('birthday')

        if datetime.now().year - cleaned_data.year < 15:
            raise forms.ValidationError("15 yaşından küçük kullanıcıların kullanması uygun değildir.")
        return cleaned_data

    def clean_phone_number(self):
        cleaned_data = self.cleaned_data.get('phone_number')
        regex = re.compile(r'\d+')

        phone_number_list = regex.findall(cleaned_data)
        phone_number = "".join(phone_number_list)

        if len(phone_number) != 10:
            raise forms.ValidationError("Lütfen Telefon Numarası Giriniz.")

        return cleaned_data
