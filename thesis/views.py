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

    query = request.GET.get('query')
    selected_table = request.GET.get('table')
    uni_table = request.GET.get('unitable')
    ins_table = request.GET.get('instable')
    thesisNo_string = request.GET.get('thesisno')
    title_string = request.GET.get('title')
    abstract_string = request.GET.get('abstract')
    #TODO add  every field  to the template so that we can search by every field
    #later on  I will stack if statements to filter the Thsesis.objects.all() by the selected table
    
    
    print(selected_table)
    print(uni_table)
    #show foreign key tables in the search page
    university = University.objects.all().order_by('name')
    institute = Institute.objects.all().order_by('name')

    if len(str(thesisNo_string)) <= 7 and len(str(thesisNo_string))>0: #this way we can check if the thesis number is valid or not    
        try:
            thesisno = Thesis.objects.get(thesis_no=thesisNo_string) # burayı neden yaptığımı hatırlamıyorum şuanlık önemsiz
        except Thesis.DoesNotExist:
            thesisno = None
            pass
    else:
        thesisno = None
   
    if query and selected_table:
        if selected_table == 'title':
            thesis = Thesis.objects.all().filter(title__icontains=query)
            results = thesis
        elif selected_table == 'author':
            thesis = Thesis.objects.all().filter(author__name__icontains=query)
            results = thesis
        elif selected_table == 'field':  # Add this case for the 'field' table
            thesis = Thesis.objects.all().filter(field__icontains=query)
            results = thesis
        elif selected_table == 'year':  # Add this case for the 'year' table
            thesis = Thesis.objects.all().filter(year__icontains=query)
            results = thesis
        elif selected_table == 'institute':  # Add this case for the 'institute' table
            thesis = Thesis.objects.all().filter(institute__name__icontains=query)
            results = thesis
        # Add other cases for other tables here
        else:
            results = None
    else:
        results = None

    context = {
        'thesisno': thesisno,
        'query': query,
        'university': university,
        'selected_table': selected_table,
        'results': results,
        'institute': institute,
    }
    
    print(results)

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