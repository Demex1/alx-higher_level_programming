#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except TypeError  as Er:
        print("Exception: {}".format(Er),file=sys.stderr)
        return False 
