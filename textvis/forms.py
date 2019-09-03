from django import forms


class DocForm(forms.Form):
    name = forms.CharField(label='Document Name', max_length=64)
    text = forms.CharField(label='Document Text', widget=forms.Textarea(attrs={'cols':'100', 'rows':'40'}))
