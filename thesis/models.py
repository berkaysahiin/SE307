from django.db import models

class University(models.Model):
    university_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)  # Fix the typo in max_length
    establishment_year = models.SmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(establishment_year__gt=0),
                name='establishment_year_positive_check'
            )
        ]