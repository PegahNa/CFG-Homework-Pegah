def get_file_content(file_name):
    """
    Read content of a file
    :param file_name: str file name or path
    :return: list of str where each str is a line

    Example return:
        [
            '1. line',
            '2. line',
            '3. line',
        ]
    """
    with open(file_name, 'r') as file:
        return file.readlines()


def increment_line_number(file_name):
    content = get_file_content(file_name)
    num = int(content.pop().split('.')[0])
    return num + 1
