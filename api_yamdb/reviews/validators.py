from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class UsernameRegexValidator(UnicodeUsernameValidator):
    """Валидация имени пользователя."""

    regex = r'^[\w.@+-]+\Z'
    flags = 0
    max_length = 20
    message = ('Введите правильное имя пользователя. Оно может содержать'
               ' только буквы, цифры и знаки @/./+/-/_.'
               f' Длина не более {max_length} символов')
    error_messages = {
        'invalid': f'Набор символов не более {max_length}. '
                   'Только буквы, цифры и @/./+/-/_',
        'required': 'Поле не может быть пустым',
    }


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год не может быть больше текущего.'),
            params={'value': value}
        )
