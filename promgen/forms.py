from django import forms
from pkg_resources import working_set

from promgen import models


class ExporterForm(forms.ModelForm):
    class Meta:
        model = models.Exporter
        exclude = ['project']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        exclude = []


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        exclude = ['service', 'farm']


class RuleForm(forms.ModelForm):
    class Meta:
        model = models.Rule
        exclude = ['service']


class FarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        exclude = ['source']


class SenderForm(forms.ModelForm):
    sender = forms.ChoiceField(choices=[
        (entry.module_name, entry.module_name) for entry in working_set.iter_entry_points('promgen.sender')
    ])

    class Meta:
        model = models.Sender
        exclude = ['project']


class HostForm(forms.Form):
    hosts = forms.CharField(widget=forms.Textarea)