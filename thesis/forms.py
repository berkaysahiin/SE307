import datetime
import random
from django import forms
from .models import Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University, Institute, Language
from thesis import models

class SearchForm(forms.Form):
    widgets = {
        'submission_beginning_date': forms.DateInput(attrs={'type': 'date'}),
        'submission_ending_date': forms.DateInput(attrs={'type': 'date'}),
    }
    institute_list = Institute.objects.all().order_by("name")
    a = {}
    b = []
    for institutes in institute_list:
        if institutes.name not in a: 
            a[institutes.name] = institutes.institute_id
            b.append(institutes.institute_id)
    del a 
    institute_list = institute_list.filter(institute_id__in=b)
    del b
        
        
    
    thesisno = forms.IntegerField(initial=1000000,min_value=1000000,required=False)
    title = forms.CharField(required=False)
    author = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    superviser = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    cosuperviser = forms.ModelChoiceField(queryset=Person.objects.all().order_by("surname"), required=False)
    type = forms.ModelChoiceField(queryset=Type.objects.all().order_by("type_name"), required=False)
    language = forms.ModelChoiceField(queryset=Language.objects.all().order_by("language_name"), required=False)  # assuming you have a Language model
    university = forms.ModelChoiceField(queryset=University.objects.all().order_by("name"), required=False)#TODO fix institute appearing twice
    institute = forms.ModelChoiceField(institute_list, required=False)  
    submission_beginning_date = forms.DateField(
        required=False, 
        initial='2010-12-23',
        widget=forms.DateInput(attrs={'type': 'date'})  # use the custom widget here
    )
    submission_ending_date = forms.DateField(
        required=False, 
        initial='2010-12-23',
        widget=forms.DateInput(attrs={'type': 'date'})  # use the custom widget here
    )
    number_of_pages_min = forms.IntegerField(required=False)
    number_of_pages_max = forms.IntegerField(required=False)
    abstract = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols':75}),required=False)
    YEARS_CHOICES = [
        ("at_this_date", 'at this date'),
        ("before_this_date", 'before this date'),
        ("after_this_date", 'after this date')
    ]

    years_choice = forms.ChoiceField(choices=YEARS_CHOICES, required=False, widget=forms.Select)
    year = forms.IntegerField(required=False)


class ThesisForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), required=False)
    keywords = forms.CharField(max_length=255, required=False, help_text='Enter keywords separated by commas.')

    class Meta:
        model = Thesis
        exclude = ['thesis_no', 'submission_date']


    def __init__(self, *args, **kwargs):
        super(ThesisForm, self).__init__(*args, **kwargs)
        
        self.fields['author'].queryset = Person.objects.all()
        self.fields['type'].queryset = Type.objects.all()
        self.fields['cosuperviser'].queryset = Person.objects.all()
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
        if not self.instance.pk: 
            self.instance.thesis_no = generate_unique_thesis_no()

        if not self.instance.submission_date:
            self.instance.submission_date = datetime.date.today()

        thesis = super().save(commit=commit)

        subjects = self.cleaned_data.get('subjects', [])
        ThesisSubject.objects.filter(thesis_no=thesis).delete()
        for subject in subjects:
            ThesisSubject.objects.create(thesis_no=thesis, subject=subject)

        keywords = self.cleaned_data.get('keywords', '')
        keyword_list = [keyword.strip() for keyword in keywords.split(',')]
        
        ThesisKeyword.objects.filter(thesis_no=thesis).delete()

        for keyword in keyword_list:
            ThesisKeyword.objects.create(thesis_no=thesis, keyword=keyword)

        return thesis

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['person_id']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)


        if self.instance:
            print("---------------INSTANCE-*---------------------")
            print(self.instance.person_id)


    def save(self, commit=True):
        if not self.instance.pk: 
            self.instance.person_id = generate_unique_person_id()

        person = super().save(commit=commit)

        return person


class CreateUniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'establishment_year']

    def save(self, commit=True):
        self.instance.university_id = generate_unique_university_id()
        uni = super().save(commit=commit)
        return uni

class CreateInstituteForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']

    def save(self, commit=True):
        self.instance.institute_id = generate_unique_institute_id()
        inst = super().save(commit=commit)
        return inst

# --- UTILITIES ---

def generate_unique_thesis_no():
    while True:
        new_thesis_no = random.randint(1, 1000000)

        if not Thesis.objects.filter(thesis_no=new_thesis_no).exists():
            return new_thesis_no

def generate_unique_person_id():
    while True:
        new_id = random.randint(1,10000)

        if not Person.objects.filter(person_id=new_id).exists():
            return new_id

def generate_unique_university_id():
    while True:
        new_id = random.randint(1,10000)

        if not University.objects.filter(university_id=new_id).exists():
            return new_id

def generate_unique_institute_id():
    while True:
        new_id = random.randint(1,10000)

        if not Institute.objects.filter(Institute_id=new_id).exists():
            return new_id