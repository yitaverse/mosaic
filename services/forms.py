from crispy_forms.helper import FormHelper
from services.models import Service
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.layout import Submit, Layout, Field


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['type', 'name', 'description', 'price', 'time', 'add_on']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
