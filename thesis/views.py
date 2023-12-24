from django.views.generic import ListView, DetailView
from .models import Institute, Language, Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University
from django.shortcuts import render

class InstituteListView(ListView):
    model = Institute
    template_name = 'institute_list.html'

class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'institute_detail.html'

class LanguageListView(ListView):
    model = Language
    template_name = 'language_list.html'

class LanguageDetailView(DetailView):
    model = Language
    template_name = 'language_detail.html'

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'

class ThesisListView(ListView):
    model = Thesis
    template_name = 'thesis_list.html'

class ThesisDetailView(DetailView):
    model = Thesis
    template_name = 'thesis_detail.html'

class ThesisKeywordListView(ListView):
    model = ThesisKeyword
    template_name = 'thesiskeyword_list.html'

class ThesisKeywordDetailView(DetailView):
    model = ThesisKeyword
    template_name = 'thesiskeyword_detail.html'

class ThesisSubjectListView(ListView):
    model = ThesisSubject
    template_name = 'thesissubject_list.html'

class ThesisSubjectDetailView(DetailView):
    model = ThesisSubject
    template_name = 'thesissubject_detail.html'

class TypeListView(ListView):
    model = Type
    template_name = 'type_list.html'

class TypeDetailView(DetailView):
    model = Type
    template_name = 'type_detail.html'

class UniversityListView(ListView):
    model = University
    template_name = 'university_list.html'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'

def main(request):
    return render(request, 'main.html')