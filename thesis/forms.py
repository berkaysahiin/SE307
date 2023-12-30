# forms.py in your 'thesis' app
from django import forms
from .models import Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University, Institute, Language

class SearchForm(forms.Form):
    thesisno = forms.IntegerField(initial=1000000,min_value=1000000,required=False)
    title = forms.CharField(required=False)
    
    author = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    superviser = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    cosuperviser = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    type = forms.ModelChoiceField(queryset=Type.objects.all().order_by("type_name"), required=False)
    language = forms.ModelChoiceField(queryset=Language.objects.all().order_by("language_name"), required=False)  # assuming you have a Language model
    university = forms.ModelChoiceField(queryset=University.objects.all().order_by("name"), required=False)#TODO fix institute appearing twice
    institute = forms.ModelChoiceField(queryset=Institute.objects.all().order_by("name"), required=False) #TODO maybe connect institute to university 
    beginning_date = forms.DateField(required=False, initial='2010-12-23',help_text='Enter Date as yyyy-mm-dd')
    ending_date = forms.DateField(required=False, initial='2010-12-23',help_text='Enter Date as yyyy-mm-dd',)
    number_of_pages_min = forms.IntegerField(required=False)
    number_of_pages_max = forms.IntegerField(required=False)
    abstract = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols':75}),required=False)


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

            initial_subjects = ThesisSubject.objects.filter(thesis_no=self.instance).values_list('subject', flat=True)
            self.fields['subjects'].initial = initial_subjects

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