#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = list_length
    length = 0
    div = my_list_1 / my_list_2
    for i in range(0, length):
        try:
           print("{:d}".format(div), end="")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except ValueError:
            return 0
        except IndexError:
            print("out of range")
        finally:
            return length
