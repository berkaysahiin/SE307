# Generated by Django 4.2 on 2023-12-24 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('institute_id', models.IntegerField(db_column='INSTITUTE_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='Turkish_CI_AS', db_column='NAME', max_length=255)),
            ],
            options={
                'db_table': 'INSTITUTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.IntegerField(db_column='LANGUAGE_ID', primary_key=True, serialize=False)),
                ('language_name', models.CharField(db_collation='Turkish_CI_AS', db_column='LANGUAGE_NAME', max_length=255)),
            ],
            options={
                'db_table': 'LANGUAGE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(db_column='PERSON_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='Turkish_CI_AS', db_column='NAME', max_length=255)),
                ('surname', models.CharField(db_collation='Turkish_CI_AS', db_column='SURNAME', max_length=255)),
                ('birth_date', models.DateField(db_column='BIRTH_DATE')),
            ],
            options={
                'db_table': 'PERSON',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(db_column='SUBJECT_ID', primary_key=True, serialize=False)),
                ('topic', models.CharField(db_collation='Turkish_CI_AS', db_column='TOPIC', max_length=1000)),
            ],
            options={
                'db_table': 'SUBJECT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('thesis_no', models.DecimalField(db_column='THESIS_NO', decimal_places=0, max_digits=7, primary_key=True, serialize=False)),
                ('title', models.CharField(db_collation='Turkish_CI_AS', db_column='TITLE', max_length=500)),
                ('abstract', models.CharField(db_collation='Turkish_CI_AS', db_column='ABSTRACT', max_length=4000)),
                ('year', models.SmallIntegerField(db_column='YEAR')),
                ('number_of_pages', models.IntegerField(db_column='NUMBER_OF_PAGES')),
                ('submission_date', models.DateField(db_column='SUBMISSION_DATE')),
            ],
            options={
                'db_table': 'THESIS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.IntegerField(db_column='TYPE_ID', primary_key=True, serialize=False)),
                ('type_name', models.CharField(db_collation='Turkish_CI_AS', db_column='TYPE_NAME', max_length=255)),
            ],
            options={
                'db_table': 'TYPE',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='ThesisKeyword',
            fields=[
                ('thesis_no', models.OneToOneField(db_column='THESIS_NO', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='thesis.thesis')),
                ('keyword', models.CharField(db_collation='Turkish_CI_AS', db_column='KEYWORD', max_length=255)),
            ],
            options={
                'db_table': 'THESIS_KEYWORD',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThesisSubject',
            fields=[
                ('thesis_no', models.OneToOneField(db_column='THESIS_NO', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='thesis.thesis')),
            ],
            options={
                'db_table': 'THESIS_SUBJECT',
                'managed': False,
            },
        ),
    ]
