from django import forms

class EnrollForm(forms.Form):
    secret_code = forms.CharField(label='Secret Code', max_length=64, help_text='Enter the short (6 character) random code supplied by your instructor to identify your class')
