# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Institute(models.Model):
    institute_id = models.IntegerField(db_column='INSTITUTE_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    university = models.ForeignKey('University', models.DO_NOTHING, db_column='UNIVERSITY_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSTITUTE'

    def __str__(self) -> str:
        return f'{self.name}'


class Language(models.Model):
    language_id = models.IntegerField(db_column='LANGUAGE_ID', primary_key=True)  # Field name made lowercase.
    language_name = models.CharField(db_column='LANGUAGE_NAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LANGUAGE'

    def __str__(self):
        return f'{self.language_name}'


class Person(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    surname = models.CharField(db_column='SURNAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERSON'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Subject(models.Model):
    subject_id = models.IntegerField(db_column='SUBJECT_ID', primary_key=True)  # Field name made lowercase.
    topic = models.CharField(db_column='TOPIC', max_length=1000, db_collation='Turkish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBJECT'

    def __str__(self) -> str:
        return f'{self.topic}'


class Thesis(models.Model):
    thesis_no = models.DecimalField(db_column='THESIS_NO', primary_key=True, max_digits=7, decimal_places=0)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=500, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    abstract = models.CharField(db_column='ABSTRACT', max_length=4000, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    author = models.ForeignKey(Person, models.DO_NOTHING, db_column='AUTHOR_ID')  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='YEAR')  # Field name made lowercase.
    type = models.ForeignKey('Type', models.DO_NOTHING, db_column='TYPE_ID')  # Field name made lowercase.
    university = models.ForeignKey('University', models.DO_NOTHING, db_column='UNIVERSITY_ID')  # Field name made lowercase.
    institute = models.ForeignKey(Institute, models.DO_NOTHING, db_column='INSTITUTE_ID')  # Field name made lowercase.
    number_of_pages = models.IntegerField(db_column='NUMBER_OF_PAGES')  # Field name made lowercase.
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='LANGUAGE_ID')  # Field name made lowercase.
    superviser = models.ForeignKey(Person, models.DO_NOTHING, db_column='SUPERVISER', related_name='thesis_superviser_set')  # Field name made lowercase.
    cosuperviser = models.ForeignKey(Person, models.DO_NOTHING, db_column='COSUPERVISER', related_name='thesis_cosuperviser_set', blank=True, null=True)  # Field name made lowercase.
    submission_date = models.DateField(db_column='SUBMISSION_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THESIS'
    def __str__(self) -> str:
        return f'{self.thesis_no}'


class ThesisKeyword(models.Model):
    thesis_no = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='THESIS_NO', primary_key=True)  # Field name made lowercase. The composite primary key (THESIS_NO, KEYWORD) found, that is not supported. The first column is selected.
    keyword = models.CharField(db_column='KEYWORD', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THESIS_KEYWORD'
        unique_together = (('thesis_no', 'keyword'),)

    def __str__(self) -> str:
        return f'{self.keyword}'


class ThesisSubject(models.Model):
    thesis_no = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='THESIS_NO', primary_key=True)  # Field name made lowercase. The composite primary key (THESIS_NO, SUBJECT_ID) found, that is not supported. The first column is selected.
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='SUBJECT_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THESIS_SUBJECT'
        unique_together = (('thesis_no', 'subject'),)


class Type(models.Model):
    type_id = models.IntegerField(db_column='TYPE_ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPE'
    
    def __str__(self) -> str:
        return f'{self.type_name}'


class University(models.Model):
    university_id = models.IntegerField(db_column='UNIVERSITY_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    establishment_year = models.SmallIntegerField(db_column='ESTABLISHMENT_YEAR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNIVERSITY'

    def __str__(self) -> str:
        return f'{self.name}'
