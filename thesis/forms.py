# forms.py in your 'thesis' app
from django import forms
from .models import Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class ThesisForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), required=False)
    keywords = forms.CharField(max_length=255, required=False, help_text='Enter keywords separated by commas.')

    class Meta:
        model = Thesis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ThesisForm, self).__init__(*args, **kwargs)
        
        # Customize queryset for Author, Type, Cosuperviser, etc.
        self.fields['author'].queryset = Person.objects.all()
        self.fields['type'].queryset = Type.objects.all()
        self.fields['cosuperviser'].queryset = Person.objects.all()

        # Set the queryset for the subjects field
        self.fields['subjects'].queryset = Subject.objects.all()

        if self.instance:
            initial_keywords = ', '.join(
                ThesisKeyword.objects.filter(thesis_no=self.instance).values_list('keyword', flat=True)
            )
            self.fields['keywords'].initial = initial_keywords
            print(self.fields['keywords'].initial)
        else:
            print('self.instance does not exist') 

        

    def save(self, commit=True):
        # Save the main Thesis model
        thesis = super().save(commit=commit)

        # Save the related subjects
        subjects = self.cleaned_data.get('subjects', [])
        ThesisSubject.objects.filter(thesis_no=thesis).delete()
        for subject in subjects:
            ThesisSubject.objects.create(thesis_no=thesis, subject=subject)

        # Save the keywords
        keywords = self.cleaned_data.get('keywords', '')
        keyword_list = [keyword.strip() for keyword in keywords.split(',')]
        
        # Clear existing keywords for the thesis
        ThesisKeyword.objects.filter(thesis_no=thesis).delete()

        # Add new keywords
        for keyword in keyword_list:
            ThesisKeyword.objects.create(thesis_no=thesis, keyword=keyword)

        return thesis