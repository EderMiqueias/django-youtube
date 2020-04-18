from django import forms

class ContatoForm(forms.Form):
    titulo = forms.CharField(label='Title')
    tema = forms.CharField(label='Theme')
    url = forms.CharField(label='YouTube URL Video')

