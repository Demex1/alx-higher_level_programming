#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = 0
    div = []
    for i in range(0, list_length):
        try:
            length = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            length = 0
            print("division by 0")
        except TypeError:
            length = 0
            print("wrong type")
        except IndexError:
            length = 0
            print("out of range")
        finally:
            pass
        div.append(length)
    return div
