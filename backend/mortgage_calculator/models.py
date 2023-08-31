from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Mortgage(models.Model):
    principal_amount = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0)],
    )
    interest_rate = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0)],
    )
    down_payment = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
    )
    loan_term = models.IntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1)],
    )
    monthly_payment = models.FloatField(blank=True)
    total_loan_amount = models.FloatField(blank=True)
    total_mortgage_amount = models.FloatField(blank=True)
    total_interest_paid = models.FloatField(blank=True)
