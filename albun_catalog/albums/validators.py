

'''
It should have at least 2 characters and maximum - 15 characters.
▪ The username can consist only of letters, numbers, and underscore ("_"). Otherwise, raise
a ValidationError with the message:
'''
from django.core.exceptions import ValidationError


class UsernameValidator:
    def __call__(self, value):
        if len(value) < 2 or len(value) > 15:
            if not value.isalnum() and not '_' in value:
                raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")