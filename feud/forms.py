from django import forms
from django.forms import ModelForm

from .models import Prompt

class PromptForm(forms.Form):
    name = forms.CharField(label='Document Name', max_length=64)
    text = forms.CharField(label='Document Text', widget=forms.Textarea(attrs={'cols':'80', 'rows':'40'}))

class EditPromptForm(ModelForm):
    class Meta:
        vote_choices = [
        (0, 'Waiting to Vote'),
        (1, 'Voting Open'),
        (2, 'Voting Complete'),
        ]
        model = Prompt
        fields = ['name', 'text', 'is_accepting_votes']

class ResponseForm(forms.Form):
        text = forms.CharField(label='Document Text', widget=forms.Textarea(attrs={'cols':'80', 'rows':'20'}))
