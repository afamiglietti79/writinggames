from django import forms
from captcha.fields import ReCaptchaField

class DocForm(forms.Form):
    name = forms.CharField(label='Document Name', max_length=64)
    text = forms.CharField(label='Document Text', widget=forms.Textarea(attrs={'cols':'100', 'rows':'40'}))
    captcha = ReCaptchaField()
