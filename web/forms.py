from django import forms
from .models import Apply


class ApplyForm(forms.ModelForm):
    email = forms.EmailField(error_messages={"invalid": "Iltimos, to'g'ri elektron manzilni kiriting."})

    class Meta:
        model = Apply
        fields = '__all__'
