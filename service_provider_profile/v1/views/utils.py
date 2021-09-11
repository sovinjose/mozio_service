"""
File to write helper function and pre-defined values
"""
import re


MODEL_KEYS = ['name', 'email', 'phone_number', 'language', 'currency']
PROVIDER_LOCATION = ['profile_pk', 'location_name', 'longitude', 'latitude', 'price']
EMAIL_REGEX  = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PHONE_REGEX = r'((0|91)?\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'


def error_message(message):
    """
    :param message:
    :return:
    """
    return {
                'Error': {'message': message}
    }


def validate_payload(data):
    """
    :param data:
    :return:
    """
    out = list(set(MODEL_KEYS) - set(data.keys()))
    if len(out)>0:
        return False, '{} Filelds are missing'.format(' '.join(out))

    if not(re.fullmatch(EMAIL_REGEX, data['email'])):
        return False, '{} Invalid email address'
    if not(re.fullmatch(PHONE_REGEX, data['phone_number'])):
        return False, '{} Invalid phone number'

    data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone_number': data.get('phone_number'),
            'language': data.get('language'),
            'currency': data.get('currency'),
            
        }
    return True, 


def validate_provider_location(data):
    """
    :param data:
    :return:
    """
    out = list(set(PROVIDER_LOCATION) - set(data.keys()))
    if len(out)>0:
        return False, '{} Filelds are missing'.format(' '.join(out))

    data = {
            'profile': data.get('profile_pk'),
            'location_name': data.get('location_name'),
            'longitude': data.get('longitude'),
            'latitude': data.get('latitude'),
            'price': data.get('price')            
        }
    return True, data







