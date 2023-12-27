# forms.py in your 'thesis' app
from django import forms
from .models import Person, Thesis, Type

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ThesisForm, self).__init__(*args, **kwargs)
        
        # Customize queryset for Author, Type, Cosuperviser, etc.
        self.fields['author'].queryset = Person.objects.all()
        self.fields['type'].queryset = Type.objects.all()
        self.fields['cosuperviser'].queryset = Person.objects.all()