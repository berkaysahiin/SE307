from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.views.generic import ListView, DetailView
from thesis.forms import InstituteForm, LanguageForm, SubjectForm, UniversityForm, PersonForm, ThesisForm, SearchForm,  RegistrationForm
from .models import Institute, Language, Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


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

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     context = {}
#     context['form'] = form
#     return render(request, 'login.html', context)

def sign_up(request):
    print("view")
    if request.method == 'POST':
        print("post")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            login(request, user)
            return redirect('/search')
    else:
        print("get")
        form = RegistrationForm()
        context = {}
        context['form'] = form
        return render(request, 'sign_up.html', context)


def search_view(request):
    context = {}
    changed = False
    if request.method == 'GET':
        form = SearchForm(request.GET)  
        if form.is_valid():
            thesis_no = form.cleaned_data['thesisno']
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            superviser = form.cleaned_data['superviser']
            cosuperviser = form.cleaned_data['cosuperviser']
            type = form.cleaned_data['type']
            language = form.cleaned_data['language']
            university = form.cleaned_data['university']
            institute = form.cleaned_data['institute']
            submission_beginning_date = form.cleaned_data['submission_beginning_date']
            submission_ending_date = form.cleaned_data['submission_ending_date']
            number_of_pages_max = form.cleaned_data['number_of_pages_max']
            number_of_pages_min = form.cleaned_data['number_of_pages_min']
            years_choice = form.cleaned_data['years_choice']
            year = form.cleaned_data['year']
            keywords = form.cleaned_data['keywords']
            results = None
            thesis = Thesis.objects.all()

            if thesis_no != None and int(thesis_no) < 1000000:
                thesis = thesis.filter(thesis_no=thesis_no) 
                changed = True
            if title != None and title != '':
                thesis = thesis.filter(title__icontains=title)
                changed = True
            if author != None:
                thesis = thesis.filter(author=author)
                changed = True
            if superviser != None:
                thesis = thesis.filter(superviser=superviser)
                changed = True
            if cosuperviser != None:
                thesis = thesis.filter(cosuperviser=cosuperviser)
                changed = True
            if type != None:
                thesis = thesis.filter(type=type)
                changed = True
            if language != None:
                thesis = thesis.filter(language=language)
                changed = True
            if university != None:
                if institute != None:
                    thesis = thesis.filter(university=university, institute__name__contains=institute.name) #TODO maybe instead of this make user choose institute in the form
                thesis = thesis.filter(university=university)
                changed = True
            if institute != None:
                thesis = thesis.filter(institute__name__contains=institute.name)
                changed = True
            if submission_beginning_date != None:
                thesis = thesis.filter(submission_date__gte=submission_beginning_date)
                changed = True
            if submission_ending_date != None:
                thesis = thesis.filter(submission_date__lte=submission_ending_date)
                changed = True
            if number_of_pages_max != None:
                thesis = thesis.filter(number_of_pages__lte=number_of_pages_max)
                changed = True
            if number_of_pages_min != None:
                thesis = thesis.filter(number_of_pages__gte=number_of_pages_min)
                changed = True 
            if years_choice != None:
                if year != None:
                    if years_choice == 'at_this_date':
                        thesis = thesis.filter(year=year)
                    elif years_choice == 'before_this_date':
                        thesis = thesis.filter(year__lte=year)
                    elif years_choice == 'after_this_date':
                        thesis = thesis.filter(year__gte=year)
                    changed = True
            if keywords != None and keywords != '':
                keywords = keywords.split(',')
                q_objects = Q()
                for keyword in keywords:
                    q_objects |= Q(thesiskeyword__keyword__icontains=keyword)
                thesis = thesis.filter(q_objects).distinct()
                changed = True
                                    
    if changed == False:
        thesis = None
                                    
    results = thesis
    context['results'] = results #results will be a list of Thesis objects but for now it is None
    context['form'] = form


    return render(request, 'search_results.html', context)
 
# --- THESIS ---

class ThesisCreateView(LoginRequiredMixin,CreateView):
    model = Thesis
    template_name = 'thesis_form.html'
    form_class = ThesisForm
    success_url = '/thesis' 

class ThesisUpdateView(LoginRequiredMixin,UpdateView):
    model = Thesis
    template_name = 'thesis_form.html'
    form_class = ThesisForm
    success_url = '/thesis' 

class ThesisDeleteView(LoginRequiredMixin,DeleteView):
    model = Thesis
    template_name = 'delete_confirm.html'
    success_url = '/thesis' 

# --- PERSON ---

class PersonCreateView(LoginRequiredMixin,CreateView):
    model = Person
    template_name = 'person_form.html'
    form_class = PersonForm
    success_url = '/person' 

class PersonUpdateView(LoginRequiredMixin,UpdateView):
    model = Person
    template_name = 'person_form.html'
    form_class = PersonForm
    success_url = '/person' 

class PersonDeleteView(LoginRequiredMixin,DeleteView):
    model = Person
    template_name = 'delete_confirm.html'
    success_url = '/person' 

# --- UNIVERSITY --- 

class UniversityCreateView(LoginRequiredMixin,CreateView):
    model = University
    template_name =  'university_form.html'
    form_class = UniversityForm
    success_url = '/university'

class UniversityUpdateView(LoginRequiredMixin,UpdateView):
    model = University
    template_name =  'university_form.html'
    form_class = UniversityForm
    success_url = '/university'

class UniversityDeleteView(LoginRequiredMixin,DeleteView):
    model = University
    template_name = 'delete_confirm.html'
    success_url = '/university/' 

# --- INSTITUTE --- 

class InstituteCreateView(LoginRequiredMixin,CreateView):
    model = Institute
    template_name =  'institute_form.html'
    form_class = InstituteForm
    success_url = '/institute'

# --- SUBJECT ---
    
class SubjectCreateView(LoginRequiredMixin,CreateView):
    model = Subject
    template_name =  'subject_form.html'
    form_class = SubjectForm
    success_url = '/subject'

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name =  'subject_form.html'
    form_class = SubjectForm
    success_url = '/subject'

class SubjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Subject
    template_name = 'delete_confirm.html'
    success_url = '/subject/' 

# --- Language ---

class LanguageCreateView(LoginRequiredMixin,CreateView):
    model = Language
    template_name =  'language_form.html'
    form_class = LanguageForm
    success_url = '/language'


class LanguageUpdateView(LoginRequiredMixin,UpdateView):
    model = Language
    template_name =  'language_form.html'
    form_class = LanguageForm
    success_url = '/language'

class LanguageDeleteView(LoginRequiredMixin,DeleteView):
    model = Language
    template_name = 'delete_confirm.html'
    success_url = '/language/' 

# --- ERROR ---

class ErrorPageView(TemplateView):
    template_name = 'error_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_message'] = "An error occurred."
        return context 