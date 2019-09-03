from django import forms

class ScrabbleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        customchoices = kwargs.pop('customchoices')
        super(ScrabbleForm, self).__init__(*args, **kwargs)
        for key, value in customchoices.items():
            self.fields[key] = forms.ChoiceField(choices=value)
