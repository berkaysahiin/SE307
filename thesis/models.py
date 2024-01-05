from django.db import models

class Institute(models.Model):
    institute_id = models.IntegerField(db_column='INSTITUTE_ID', primary_key=True) 
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  

    class Meta:
        managed = False
        db_table = 'INSTITUTE'

    def __str__(self) -> str:
        return f'{self.name}'


class Language(models.Model):
    language_id = models.IntegerField(db_column='LANGUAGE_ID', primary_key=True) 
    language_name = models.CharField(db_column='LANGUAGE_NAME', max_length=255, db_collation='Turkish_CI_AS')  

    class Meta:
        managed = False
        db_table = 'LANGUAGE'

    def __str__(self):
        return f'{self.language_name}'


class Person(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', primary_key=True)  
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  
    surname = models.CharField(db_column='SURNAME', max_length=255, db_collation='Turkish_CI_AS')  
    birth_date = models.DateField(db_column='BIRTH_DATE')  

    class Meta:
        managed = False
        db_table = 'PERSON'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Subject(models.Model):
    subject_id = models.IntegerField(db_column='SUBJECT_ID', primary_key=True)  
    topic = models.CharField(db_column='TOPIC', max_length=1000, db_collation='Turkish_CI_AS')  

    class Meta:
        managed = False
        db_table = 'SUBJECT'

    def __str__(self) -> str:
        return f'{self.topic}'


class Thesis(models.Model):
    thesis_no = models.DecimalField(db_column='THESIS_NO', primary_key=True, max_digits=7, decimal_places=0)  
    title = models.CharField(db_column='TITLE', max_length=500, db_collation='Turkish_CI_AS')  
    abstract = models.CharField(db_column='ABSTRACT', max_length=4000, db_collation='Turkish_CI_AS')  
    author = models.ForeignKey(Person, on_delete=models.PROTECT, db_column='AUTHOR_ID')  
    year = models.SmallIntegerField(db_column='YEAR')  
    type = models.ForeignKey('Type', models.PROTECT, db_column='TYPE_ID')  
    university = models.ForeignKey('University', models.PROTECT, db_column='UNIVERSITY_ID')  
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, db_column='INSTITUTE_ID', null=True)  
    number_of_pages = models.IntegerField(db_column='NUMBER_OF_PAGES') 
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, db_column='LANGUAGE_ID', null=True) 
    superviser = models.ForeignKey(Person, on_delete=models.SET_NULL, db_column='SUPERVISER', related_name='thesis_superviser_set', null=True)  # Field name made lowercase.
    cosuperviser = models.ForeignKey(Person, on_delete=models.SET_NULL, db_column='COSUPERVISER', related_name='thesis_cosuperviser_set', blank=True, null=True)  # Field name made lowercase.
    submission_date = models.DateField(db_column='SUBMISSION_DATE')  

    @property
    def keywords(self):
        return ThesisKeyword.objects.filter(thesis_no=self.thesis_no).values_list('keyword', flat=True)

    @property
    def subjects(self):
        return Subject.objects.filter(thesissubject__thesis_no=self.thesis_no).values_list('topic', flat=True)

    class Meta:
        managed = False
        db_table = 'THESIS'
    def __str__(self) -> str:
        return f'{self.thesis_no}'


class ThesisKeyword(models.Model):
    thesis_no = models.OneToOneField(Thesis, on_delete=models.CASCADE, db_column='THESIS_NO', primary_key=True)
    keyword = models.CharField(db_column='KEYWORD', max_length=255, db_collation='Turkish_CI_AS')  

    class Meta:
        managed = False
        db_table = 'THESIS_KEYWORD'
        unique_together = (('thesis_no', 'keyword'),)

    def __str__(self) -> str:
        return f'{self.keyword}'


class ThesisSubject(models.Model):
    thesis_no = models.OneToOneField(Thesis, on_delete=models.CASCADE, db_column='THESIS_NO', primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='SUBJECT_ID')


    class Meta:
        managed = False
        db_table = 'THESIS_SUBJECT'
        unique_together = (('thesis_no', 'subject'),)


class Type(models.Model):
    type_id = models.IntegerField(db_column='TYPE_ID', primary_key=True)  
    type_name = models.CharField(db_column='TYPE_NAME', max_length=255, db_collation='Turkish_CI_AS')  

    class Meta:
        managed = False
        db_table = 'TYPE'
    
    def __str__(self) -> str:
        return f'{self.type_name}'


class University(models.Model):
    university_id = models.IntegerField(db_column='UNIVERSITY_ID', primary_key=True)  
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  
    establishment_year = models.SmallIntegerField(db_column='ESTABLISHMENT_YEAR')  

    class Meta:
        managed = False
        db_table = 'UNIVERSITY'

    @property
    def institutes(self):
        institute_ids = UniversityInstitute.objects.filter(university_id=self.university_id).values_list('institute_id', flat=True)
        return Institute.objects.filter(institute_id__in=institute_ids)

    def __str__(self) -> str:
        return f'{self.name}'

class UniversityInstitute(models.Model):
    university_id = models.OneToOneField(University, on_delete=models.CASCADE, db_column='UNIVERSITY_ID', primary_key=True)
    institute_id = models.ForeignKey(Institute, on_delete=models.CASCADE, db_column='INSTITUTE_ID')

    class Meta:
        managed = False
        db_table = 'UNIVERSITY_INSTITUTE'
        unique_together = (('university_id', 'institute_id'),)