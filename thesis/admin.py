from django.contrib import admin

# Register your models here.
from .models import University  # Import your model
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_id', 'name', 'establishment_year')
