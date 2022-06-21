#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = 0
    div = []
    for i in range(0, list_length):
        try:
            length = my_list_1[i] / my_list_2[i]
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
            pass
        div.append(length)
    return div
