def invalid_stu_name(name):
    return not name or any(char.isdigit() or char == ' ' for char in name)


def invalid_paper_name(name):
    return not name