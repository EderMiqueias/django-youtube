from django import forms

class ContatoForm(forms.Form):
    titulo = forms.CharField(label='Title')
    CHOICES = [('1', 'music'), ('2', 'entertainment'),('3', 'news'),('4','politics'),('5','games')]
    tema = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    url = forms.CharField(label='YouTube URL Video',max_length=43,min_length=43)
