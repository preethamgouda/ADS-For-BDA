import os
import fnmatch


def cat(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            characters = 0

            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)

            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {characters}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")



def head(filename, num_lines=5):
    try:
        with open(filename, 'r') as file:
            for _ in range(num_lines):
                line = file.readline()
                if not line:
                    break
                print(line, end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")



# def sum_file_numbers(filename):
#     try:
#         with open(filename, 'r') as file:
#             total_sum = 0
#             for line_number, line in enumerate(file, start=1):
#                 stripped_line = line.strip()
#                 if stripped_line:
#                     try:
#                         number = float(stripped_line)
#                         total_sum += number
#                     except ValueError:
#                         print(f"Warning at line {line_number}: '{stripped_line}' is not a valid number.")

#             print(f"Sum of numbers in '{filename}': {total_sum}")
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
    


def pattern_rec(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            with open(destination_filename, 'w') as destination_file:
                destination_file.write(source_file.read())
        print(f"File '{source_filename}' copied to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_filename}' not found.")



def list_files(directory="."):
    try:
        file_list = os.listdir(directory)
        for filename in file_list:
            if os.path.isfile(os.path.join(directory, filename)):
                print(filename)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    
directory = input("Enter the directory path ")
if directory:
    list_files(directory)
else:
    list_files()



def find_largest_file(directory="."):
    try:
        max_size = 0
        largest_file = None

        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_size = os.stat(file_path).st_size
                if file_size > max_size:
                    max_size = file_size
                    largest_file = file_path
        
        if largest_file:
            print(f"Largest file: {largest_file}")
        else:
            print("No files found in the directory.")
    except FileNotFoundError:
        print(f"Error: File '{source_filename}' not found.")

directory = input("Enter the directory path : ")
if directory:
    find_largest_file(directory)
else:
    find_largest_file()


def find_most_recent_file(directory="."):
    try:
        max_mtime = 0
        most_recent_file = None

        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > max_mtime:
                    max_mtime = file_mtime
                    most_recent_file = file_path
        
        if most_recent_file:
            print(f"Most recently modified file: {most_recent_file}")
        else:
            print("No files found in the directory.")
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    




def find_matching_files(directory, pattern):
    try:
        for root, _, files in os.walk(directory):
            for filename in files:
                if fnmatch.fnmatch(filename, pattern):
                    file_path = os.path.join(root, filename)
                    print(file_path)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    
    
def unique(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

lst=[1,3,3,44,4,44,55,4]

def dups(input_list):
    unique_items = set()
    duplicate_items = []
    
    for item in input_list:
        if item in unique_items:
            duplicate_items.append(item)
        else:
            unique_items.add(item)
    
    return duplicate_items

list2 = [1, 2, 2, 3, 4, 4, 5]

def group(input_list, size):
    grouped_lists = [input_list[i:i+size] for i in range(0, len(input_list), size)]
    return grouped_lists

print('1')
cat('sample.py')
print('2')
wc('sample.py')
print('3')
head('sample.py')
print('4')
#sum_file_numbers('sample.py')
print('5')
pattern='def'
print('6')
pattern_rec(pattern,'sample.py')
print('7')
copy_file('file1.txt','D:/MSIS/file2.txt')
print('8')
find_most_recent_file('D:')
print('9')
find_matching_files('D:/MSIS/ADS-LAB', 'py')
unique(lst) 
dups(list2)

group(list2,3)