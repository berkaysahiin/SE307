from django.views.generic import ListView, DetailView

from thesis.forms import ThesisForm
from .models import Institute, Language, Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University
from django.shortcuts import render
from django.db import connection
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


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


def search_view(request):
# each of this values can be None
#TODO clean this mess by dividing variables into groups by types
    thesisNo_string = request.GET.get('thesisno')
    title_string = request.GET.get('title')
    abstract_string = request.GET.get('abstract')
    author_table = request.GET.get('author')        #this is a person
    type_table = request.GET.get('type')
    language_table = request.GET.get('language')
    supervisor_table = request.GET.get('supervisor') #this is a person
    coSupervisor_table = request.GET.get('cosupervisor') #this is a person
    submitDateBegin_date = request.GET.get('beginning_date')
    submitDateEnd_date = request.GET.get('ending_date') #*date format is  yyyy-mm-dd
    numberOfPagesMin_int = request.GET.get('number_of_pages_min')
    numberOfPagesMax_int = request.GET.get('number_of_pages_max')
    uni_table = request.GET.get('unitable')
    ins_table = request.GET.get('instable')

    
    print("pages",numberOfPagesMax_int)# this is where I test if the values are working or not
    
    
    context = {}
    
    #later on  I will stack if statements to filter the Thsesis.objects.all() by the selected table
    
    #show foreign key tables in the search page
    university = University.objects.all().order_by('name')
    institute = Institute.objects.all().order_by('name')
    person = Person.objects.all().order_by('surname')
    type = Type.objects.all().order_by('type_name')
    language = Language.objects.all().order_by('language_name')
    
    
    context['university'] = university
    context['institute'] = institute
    context['person'] = person
    context['type'] = type
    context['language'] = language

    if len(str(thesisNo_string)) <= 7 and len(str(thesisNo_string))>0: #this way we can check if the thesis number is valid or not    
        try:
            thesisno = Thesis.objects.get(thesis_no=thesisNo_string) # burayı neden yaptığımı hatırlamıyorum şuanlık önemsiz
        except Thesis.DoesNotExist:
            thesisno = None
            pass
    else:
        thesisno = None
   
    context['thesisno'] = thesisno
    context['results'] = None #results will be a list of Thesis objects but for now it is None
    


    return render(request, 'search_results.html', context)
 


class ThesisCreateView(CreateView):
    model = Thesis
    template_name = 'thesis_form.html'
    form_class = ThesisForm
    success_url = reverse_lazy(ThesisListView)


class ThesisUpdateView(UpdateView):
    model = Thesis
    form_class = ThesisForm
    template_name = 'thesis_form.html'
    success_url = reverse_lazy('thesis')

