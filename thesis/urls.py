from django.urls import path
from .views import ErrorPageView, LanguageDeleteView, PersonDeleteView, SubjectDeleteView, ThesisDeleteView, UniversityDeleteView, login_view, InstituteCreateView, LanguageCreateView, LanguageUpdateView, PersonCreateView, PersonUpdateView, SubjectCreateView, SubjectUpdateView, UniversityCreateView, UniversityUpdateView, main, search_view, ThesisCreateView, ThesisUpdateView
from thesis import views

app_name = 'thesis'

urlpatterns = [
    path('', search_view, name='search'),
    path('main/', main, name='main'),
    path('login/', login_view, name='login'),
    path('institute/', views.InstituteListView.as_view(), name='institute-list'),
    path('institute/<int:pk>/', views.InstituteDetailView.as_view(), name='institute-detail'),

    path('language/', views.LanguageListView.as_view(), name='language-list'),
    path('language/<int:pk>/', views.LanguageDetailView.as_view(), name='language-detail'),

    path('person/', views.PersonListView.as_view(), name='person-list'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),

    path('subject/', views.SubjectListView.as_view(), name='subject-list'),
    path('subject/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),

    path('thesis/', views.ThesisListView.as_view(), name='thesis-list'),
    path('thesis/<int:pk>/', views.ThesisDetailView.as_view(), name='thesis-detail'),

    path('thesiskeyword/', views.ThesisKeywordListView.as_view(), name='thesiskeyword-list'),
    path('thesiskeyword/<int:pk>/', views.ThesisKeywordDetailView.as_view(), name='thesiskeyword-detail'),

    path('thesissubject/', views.ThesisSubjectListView.as_view(), name='thesissubject-list'),
    path('thesissubject/<int:pk>/', views.ThesisSubjectDetailView.as_view(), name='thesissubject-detail'),

    path('type/', views.TypeListView.as_view(), name='type-list'),
    path('type/<int:pk>/', views.TypeDetailView.as_view(), name='type-detail'),

    path('university/', views.UniversityListView.as_view(), name='university-list'),
    path('university/<int:pk>/', views.UniversityDetailView.as_view(), name='university-detail'),
    path('search/', search_view, name='search'),

    path('thesis/add/', ThesisCreateView.as_view(), name='thesis_add'),
    path('thesis/<int:pk>/edit/', ThesisUpdateView.as_view(), name='thesis_edit'),
    path('thesis/<int:pk>/delete/', ThesisDeleteView.as_view(), name='thesis_delete'),

    path('person/add', PersonCreateView.as_view(), name='person_add'),
    path('person/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('person/<int:pk>/delete/', PersonDeleteView.as_view(), name='person_delete'),

    path('university/add', UniversityCreateView.as_view(), name='university_create'),
    path('university/<int:pk>/edit', UniversityUpdateView.as_view(), name='university_update'),
    path('university/<int:pk>/delete', UniversityDeleteView.as_view(), name='university_delete'),

    path('institute/add', InstituteCreateView.as_view(), name='institute_create'),

    path('subject/add', SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/edit', SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete', SubjectDeleteView.as_view(), name='subject_delete'),

    path('language/add', LanguageCreateView.as_view(), name='language_create'),
    path('language/<int:pk>/edit', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/delete', LanguageDeleteView.as_view(), name='language_delete'),

    path('error_page/', ErrorPageView.as_view(), name='error_page'),
]
