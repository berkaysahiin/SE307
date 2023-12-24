# Generated by Django 4.2 on 2023-12-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('establishment_year', models.SmallIntegerField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='university',
            constraint=models.CheckConstraint(check=models.Q(('establishment_year__gt', 0)), name='establishment_year_positive_check'),
        ),
    ]
