def to_formal_name(firstname, lastname):
    """
    Return the formal name with lastname first then firstname in title case
    :param firstname: 'john'
    :param lastname: 'doe'
    :return: 'Doe, John'

    >>> to_formal_name('john', 'doe')
    'Doe, John'
    """
    return f"{lastname.title()}, {firstname.title()}"


def gen_email(firstname, lastname):
    """
    Return the email address based on firstname and lastname in lowercase
    :param firstname: 'john'
    :param lastname: 'doe'
    :return: 'john.doe@xcompany.com.au'

    >>> gen_email('john', 'doe')
    'john.doe@xcompany.com.au'
    """

    return f"{firstname.lower()}.{lastname.lower()}@xcompany.com.au"

print("helpers module loaded")
