from django.urls import path
from . import views
from .views import main, search_view

app_name = 'thesis'

urlpatterns = [
    path('main/', main, name='main'),
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
]
