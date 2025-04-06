#!/usr/bin/env python3

# using local module helpers.py found in the trunk directory
# /Users/mirasa/PycharmProjects/pythonProject/helpers.py
# helpers module contains the following functions:
# to_formal_name(firstname, lastname) - returns lastname first then firstname in title case
# gen_email(firstname, lastname) - returns email address based on firstname and lastname in lowercase

import argparse
import datetime
import extras
import helpers

people = [{'firstname': 'JOSE', 'lastname': 'Diaz'}, {'firstname': 'julie', 'lastname': 'ONG'}]
heroes = [{'firstname': 'steve', 'lastname': 'rogers', 'codename': 'captain america'}, {'firstname': 'tony', 'lastname': 'stark', 'codename': 'ironman'}]
nums = [2, 4, 6]

def gen_info(person):
    name = helpers.to_formal_name(person['firstname'], person['lastname'])
    email = helpers.gen_email(person['firstname'], person['lastname'])
    codename = person['codename'].upper() if 'codename' in person else None

    if codename:
        return f"Person's name is {name} and the email address is {email}... and also known as {codename}"
    else:
        return f"Person's name is {name} and the email address is {email}"


def square(x):
    """Returns the square of x.

    Args: x as int or float
    Returns: x multiplied by itself

    >>> square(2)
    2
    """
    return x * x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="running simulation on local modules",
        description="Use local module")
    parser.add_argument(
        "-e", "--environment",
        help="environment to run the process",
        required=True,
        default='test'
    ),
    parser.add_argument(
        '-t','--type',
        help="type of list to process",
        required=True,
        default='people'
    ),
    parser.add_argument(
        '-sq','--square',
        help="just take the numbers and square them",
        required=False,
        type=bool,
        default=True
    )

    args = parser.parse_args()

    print(f"!!! Running script on {args.environment} environment, please don't delete anything !!!" if args.environment == 'prod' else f"Running script on {args.environment} environment, do whatever you want")

    print(extras.start_label(datetime.datetime.now()))

    if args.type == 'people':
        for person in people:
            print(gen_info(person))
    else:
        for hero in heroes:
            print(gen_info(hero))

    print (f"Squaring values of {nums}")
    if args.square:
        for num in nums:
            print(f"Square of {num} is {square(num)}")
    else:
        print("No squaring done")

    print(extras.end_label(datetime.datetime.now()))
