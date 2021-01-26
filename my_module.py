tutorials = ['c', 'c++', 'java', 'python', 'html', 'css', 'js']

def find_tutorial(target):
    for tut in tutorials:
        if tut == target:
            return True
    return False

