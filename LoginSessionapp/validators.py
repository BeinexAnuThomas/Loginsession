from django.core.exceptions import ValidationError

def age_validation(value):
    if value < 18:
        raise ValidationError("Age must be above 18 ")