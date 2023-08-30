def reverse_words_string(string):  # definition of a Python function
    words = []   # create an empty list
    word_start = 0  # initialize the variable word_start with the value 0
    for idx in range(len(string)):  # index: 0
        char = string[idx]

        if char == " ":
            words.append(string[word_start: idx])
            word_start = idx
        elif string[word_start] == " ":
            words.append(" ")
            word_start = idx

    words.append(string[word_start:])
    reverse_list(words)
    return "".join(words)


def reverse_list(my_list):
    start = 0
    end = len(my_list) - 1
    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1