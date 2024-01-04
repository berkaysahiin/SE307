from django.contrib import admin
from .models import Institute, Language, Person, Subject, Thesis, ThesisKeyword, ThesisSubject, Type, University, UniversityInstitute

# Register your models here.
@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_id', 'name')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_id', 'language_name')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'name', 'surname', 'birth_date')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'topic')

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('thesis_no', 'title', 'author', 'year', 'type', 'university', 'institute', 'number_of_pages', 'language', 'superviser', 'cosuperviser', 'submission_date')

@admin.register(ThesisKeyword)
class ThesisKeywordAdmin(admin.ModelAdmin):
    list_display = ('thesis_no', 'keyword')

@admin.register(ThesisSubject)
class ThesisSubjectAdmin(admin.ModelAdmin):
    list_display = ('thesis_no', 'subject')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'type_name')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_id', 'name', 'establishment_year')

@admin.register(UniversityInstitute)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_id', 'institute_id')