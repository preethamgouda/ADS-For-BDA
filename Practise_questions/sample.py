import random

# 1. exchange values without using a temporary value

def exchange_val(val1,val2):
	val1,val2=val2,val1
	return val1,val2
# 2 .check if a given number is positive or not


def positive(num):
	return num>-1

# 3. print all the numbers that are divisible by a given number 

def divisibleNum(limit, num):
 	num_list=[]

 	for number in range(1,limit+1):
 		if number%num==0:
 			num_list.append(number)
 	return num_list


# 4. print All the odd numbers in given range 

def oddNum(limit):
	odd_list=[]

	for i in range (0,10):
		if i%2!=0:
			odd_list.append(i)
	return odd_list


# 5. print quotient and remainder of the given 2 numbers 

def quo_rem(num1,num2):
	return num1//num2,num1%num2


# 6.find sum of digits in a number 


def sumofdigit(num):
	sum=0
	while (num!=0):
		sum=sum+int(num%10)
		n=int(num/10)
	return sum

# 7. smallest divisor of an integer

def smallestDivisor(num):
	num_list=[]
	for i in range (2,num+1):
		if num % i ==0:
			num_list.append(i)
		#return num_list
	num_list.sort()
	return num_list[0]


#8 . python program to read a given number and compute n+nn+nnn

def compute(n):
	return n+n**2+n**3

# 9 . python program to reverse a given number

def reverse(num):
	return str(num)[::-1]


#10 . program to calculate the average of numbers given in a list

def average(lst):
	return sum(lst)/len(lst)


# 11 . pgm to count the number of digits in a number 

def count (digit):
	return len(str(digit))

# 12 . python program to check whether a pgm is palindrome or not 


def palindrome (num):
	rev=0
	while(num>0):
		dig=num%10
		rev=rev*10+digit
		num=num//10

#13

def no_of_occurnce(string,substring):
    return string.count(substring)

#14 

def point_of_occurance(string,substring):
    return string.find(substring)


#15 

def all_alphabets(string):
    if string.isalpha():
        return True
    else:
        return False

#16 

def replace_substring(string,substring,new_substring):
    return string.replace(substring,new_substring)


#17 

def no_of_vowels(string):
    count=0
    vowels=['a','e','i','o','u']
    for i in range(len(string)):
        if string[i] in vowels:
            count=count+1

    return count

#18 

def replace(string):
  
    lis = list(string.split(" "))
    string = '-'.join(lis) 
    return string

#19

#20


def larger(str1,str2):
    c1=0
    c2=0

    for i in str1:
        c1=c1+1
    for j  in str2:
        c2=c2+1

    if c1>c2:
        return str1
    else:
        return str2

#21 

def calculate_upper_lower_case(string):
    upper=0
    lower=0
    for i in string:
        if (i.islower()):
            lower

#22


def count_dig_letters(input_string):
    num_digits = 0
    num_letters = 0

    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1

    return num_digits, num_letters

#23 


def check_pattern_in_sentence(sentence, pattern):
    words = sentence.split()
    
    for word in words:
        if word == pattern:
            return True
    
    return False


#24
def cumulative_sum(input_list):
    cumulative_result = []
    sum_so_far = 0
    
    for num in input_list:
        sum_so_far += num
        cumulative_result.append(sum_so_far)
    
    return cumulative_result

#25

def generate_random_integers(count, l_b, u_b):
    random = [random.randint(l_b, u_b) for _ in range(count)] # comprehensions
    return random_integers


#26


def generate_random_integers(count, 1, 20):
    random = [random.randint(1, 20) for _ in range(count)] # comprehensions
    return random_intege


#28




def generate(count, size_n):
    if count > size_n:
        raise ValueError("Cannot generate numbers due to insufficient range.")
    
    numbers = []
    for i in range(1, count + 1):
        lower_bound = (i - 1) * range_size + 1
        upper_bound = i * range_size
        number = random.randint(l_b, u_b)
        numbers.append(number)
    
    return numbers