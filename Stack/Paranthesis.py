from stack import *

input_chars = "([{"
output_chars = ")]}"

s1 = stack()

def check_for_parentheses(input_string):
    f = 0
    for i in input_string:
        if i in input_chars:
            s1.push(i)
        elif i in output_chars:
            if not s1.isStackEmpty():
                if input_chars.index(s1.pop()) == output_chars.index(i):
                    f = 0
                else:
                    f = 1
                    break
            else:
                f = 1
                break
    return f == 0

def file_check(file_name):
    results = []
    with open('input.txt', 'r') as f:
        for line in f:
            results.append(check_for_parentheses(line))

    assert all(results)

# Test cases
assert check_for_parentheses("(({[[{{}}]]}))") == True
assert check_for_parentheses("(({{}]]}))") == False
file_check("file1.txt")
