import datetime
from functools import wraps
from flask import request
from flask_restplus import abort, ValidationError
from werkzeug import exceptions


class ValidationUtil:
    @staticmethod
    def add_errors(keyname, message, errors):
        errors.append({
            'field': keyname,
            'messsage': message,
        })

    @staticmethod
    def request_get_json(request) -> dict:
        """
        JSONで送られたリクエストボディをdictにパース
        :param request: request
        :return: request body(dict)
        """

        data = request.get_json()
        return data


def validate(validate_func, api=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors = validate_func(*args, **kwargs, api=api)
            if errors:
                abort(exceptions.BadRequest.code, errors=errors)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def str_length(length=None, max_length=None, min_length=None):
    def validate(s):
        if length is not None:
            if len(s) != length:
                raise ValidationError(f'must be {length} characters')

        if max_length is not None:
            if len(s) > max_length:
                raise ValidationError(f'must be {max_length} characters or less')

        if min_length is not None:
            if len(s) < min_length:
                raise ValidationError(f'must be at least {min_length} characters')

        return s

    return validate


def validatable_int(minimum=None, maximum=None):
    def validate(n):
        int_n = int(n)
        if minimum is not None:
            if int_n < minimum:
                raise ValidationError(f'must be greater equal {minimum} value.')

        if maximum is not None:
            if maximum < int_n:
                raise ValidationError(f'must be less equal {maximum} value.')

        return int_n

    return validate
