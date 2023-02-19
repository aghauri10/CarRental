from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(year):
    if year > 1880 and year <= timezone.now().year:
        raise ValidationError(f"{year} is not correct year!")
