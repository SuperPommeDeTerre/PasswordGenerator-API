import string
import random
import re

LETTERS_LOWERCASE = string.ascii_lowercase
LETTERS_UPPERCASE = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation

DEFAULTS = {
    'POLICY': {
        'lowercase': 1,
        'uppercase': 1,
        'digits': 1,
        'punctuation': 1,
        'excluded_chars': '',
        'length': {
            'min': 16,
            'max': 2048
        }
    },
    'CONSTRAINTS': {
        'lowercase': 1,
        'uppercase': 1,
        'digits': 1,
        'punctuation': 1,
        'excluded_chars': ''
    }
}

def get_chars_for_family(chars, count):
    '''
    '''
    return random.choices(chars, k=count)

def generate(length=16, count=5, constraints=DEFAULTS['CONSTRAINTS']):
    '''
    Generates a random password having the specified length
    :param length: length of password to be generated. (default: 16)
        if nothing is specified.
    :type length: integer
    :param count: Number of passwords to generate (default: 5)
    :type count: integer
    :return: array<string <class 'str'>>
    '''
    effective_constraints = DEFAULTS['CONSTRAINTS'] | constraints
    # create alphanumerical from string constants
    string_constant = ''
    string_constant += NUMBERS if effective_constraints['digits'] > 0 else ''
    string_constant += LETTERS_LOWERCASE if effective_constraints['lowercase'] > 0 else ''
    string_constant += LETTERS_UPPERCASE if effective_constraints['uppercase'] > 0 else ''
    string_constant += PUNCTUATION if effective_constraints['punctuation'] > 0 else ''

    # convert printable from string to list and shuffle
    string_constant = list(string_constant)
    random.shuffle(string_constant)

    return_value = []
    # generate random password and convert to string
    for _ in range(count):
        min_password = get_chars_for_family(NUMBERS, effective_constraints['digits'])
        min_password += get_chars_for_family(LETTERS_LOWERCASE, effective_constraints['lowercase'])
        min_password += get_chars_for_family(LETTERS_UPPERCASE, effective_constraints['uppercase'])
        min_password += get_chars_for_family(PUNCTUATION, effective_constraints['punctuation'])
        number_of_chars_to_padd = length - len(min_password)
        if number_of_chars_to_padd > 0:
            min_password += random.choices(string_constant, k=number_of_chars_to_padd)
        # elif len(min_password) > length:
            
        random.shuffle(min_password)
        random_password = ''.join(min_password)
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
    effective_policy = DEFAULTS['POLICY'] | policy
    is_password_valid = True
    if len(password) < effective_policy['length']['min']:
        is_password_valid = False
    if is_password_valid and len(password) > effective_policy['length']['max']:
        is_password_valid = False
    if is_password_valid and effective_policy['digits'] > 0 and re.match('.*[' + NUMBERS + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and effective_policy['lowercase'] > 0 and re.match('.*[' + LETTERS_LOWERCASE + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and effective_policy['uppercase'] > 0 and re.match('.*[' + LETTERS_UPPERCASE + '].*', password) is None:
        is_password_valid = False
    if is_password_valid and effective_policy['punctuation'] > 0 and re.match('.*[' + PUNCTUATION.replace('\\', '\\\\').replace('-', '\\-').replace('[', '\\[').replace(']', '\\]') + '].*', password) is None:
        is_password_valid = False
    return is_password_valid
