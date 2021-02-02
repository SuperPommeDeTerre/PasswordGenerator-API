import string
import random
import re

LETTERS_LOWERCASE = string.ascii_lowercase
LETTERS_UPPERCASE = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation

DEFAULTS = {
    'POLICY': {
        'use_lowercase': True,
        'use_uppercase': True,
        'use_digits': True,
        'use_punctuation': True,
        'length': {
            'min': 16,
            'max': 2048
        }
    }
}

def generate(length, count, policy=DEFAULTS['POLICY']):
    '''
    Generates a random password having the specified length
    :param length: length of password to be generated. Defaults to DEFAULTS.LENGTH
        if nothing is specified.
    :type length: integer
    :param count: Number of passwords to generate
    :type count: integer
    :return: array<string <class 'str'>>
    '''
    # create alphanumerical from string constants
    string_constant = ''
    string_constant += NUMBERS if policy['use_digits'] else ''
    string_constant += LETTERS_LOWERCASE if policy['use_lowercase'] else ''
    string_constant += LETTERS_UPPERCASE if policy['use_uppercase'] else ''
    string_constant += PUNCTUATION if policy['use_punctuation'] else ''

    # convert printable from string to list and shuffle
    string_constant = list(string_constant)
    random.shuffle(string_constant)

    return_value = []
    # generate random password and convert to string
    for i in range(count):
        random_password = random.choices(string_constant, k=length)
        random_password = ''.join(random_password)
        if (not validate(random_password)):
            i = i - 1
            continue
        return_value.append(random_password)
    return return_value

def validate(password, policy=DEFAULTS['POLICY']):
    '''
    Validate a password against a policy.

    :param password: Password to validate
    :type password: string
    :param policy: Policy to validate against.
    :type policy: object
    :return: True or False
    '''
    is_password_valid = True
    if len(password) < policy['length']['min']:
        is_password_valid = False
    if is_password_valid and len(password) > policy['length']['max']:
        is_password_valid = False
    if is_password_valid and policy['use_digits'] and re.match('.*[' + NUMBERS + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and policy['use_lowercase'] and re.match('.*[' + LETTERS_LOWERCASE + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and policy['use_uppercase'] and re.match('.*[' + LETTERS_UPPERCASE + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and policy['use_punctuation'] and re.match('.*[' + PUNCTUATION.replace('\\', '\\\\').replace('-', '\\-').replace('[', '\\[').replace(']', '\\]') + '].*', password) is None:
        is_password_valid = False
    return is_password_valid