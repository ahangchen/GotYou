def invalid_stu_name(name):
    return not name or any(char.isdigit() for char in name)

def invalid_paper_name(name):
    return not name