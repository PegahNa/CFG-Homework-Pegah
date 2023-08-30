a_list = [1, 2, 3, 4]
a_list2 = ["Sam", "Jess", "Pam"]


# print(list(reversed(a_list)))
# print(list(reversed(a_list2)))


def list_reverser(a_list):
    l_ptr = 0
    r_ptr = len(a_list) - 1
    while l_ptr < r_ptr:
        a_list[l_ptr], a_list[r_ptr] = a_list[r_ptr], a_list[l_ptr]
        l_ptr = +1
        r_ptr = -1

    return a_list

print(list_reverser(a_list2))