def largest(list):
  large=list[0]
  for i in list:
    if i>large:
      large =i
  return large

def second_largest(list):
  sublist=[x for x in list if x<max(list)]   # using comprehensions
  return max(sublist)

 # def list(lst): // using loops
 #  sub=[]
 #  for x in lst:
 #    if x<max(lst):
 #      sub.append(x)
 #  return max(sub)      

def odd_even(list):
  odd=[]
  even=[]
  for i in list:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i)
  return even, odd


 # def odd_even(list):
 #  odd=[x for x in list if x%2!=0]  # using comprehensions
 #  even=[x for x in list if x%2==0]
 #  return odd, even

def same_lists(lst1,lst2):
  lst1=set(lst1)
  lst2=set(lst2)
  if lst1==lst2:
    return True


# def lst(lst1,lst2):
#   lst1=lst1.sort()
#   lst2=lst2.sort()
#   if lst1==lst2:
#     return True


def union(lst1,lst2):
  new=[]
  for i in lst1:
    new.append(i)
  for j in lst2:
    new.append(j)
  return new



def intersection(lst1,lst2):
  new=[]
  for i in lst1:
    for j in lst2 :
      if i==j:
        new.append(i)
  return new





def remove_duplicate(lst):
  res=[]
  [res.append(x) for x in lst if x not in res]
  return res



def longest(words):
  word_list=[]
  for word in words:
    word_list.append((len(word),word))
  word_list.sort()
  return word_list[-1][1],len(word_list[-1][1])


def add_key_value(dictionary, key, value):
    dictionary[key] = value


def concatenate_dicts(dict1, dict2):
    concatenated_dict = dict1.copy()  
    concatenated_dict.update(dict2)    
    return concatenated_dict

def key_exists(dictionary, key):
    return key in dictionary


def square_diction(n):
    square_dict = {x: x*x for x in range(1, n+1)}
    return square_dict


def sum_dictionary_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum



def multiply_dictionary_values(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result


def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]



def is_empty(my_dict):
    return not bool(my_dict)


def make_dict(key_value_list):
    result_dict = {}
    for key, value in key_value_list:
        result_dict[key] = value
    return result_dict



def encrypt(phrase, cipher_dict):
    encrypted_phrase = ''
    for char in phrase:
        if char in cipher_dict:
            encrypted_phrase += cipher_dict[char]
        else:
            encrypted_phrase += char
    return encrypted_phrase

CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w',
               'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o',
               'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b',
               'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd',
               'n': 'a', 't': ' ', 'w': 't'}


def make_cipher_dict(alphabet):
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    
    cipher_dict = {}
    for original, encrypted in zip(alphabet, shuffled_alphabet):
        cipher_dict[original] = encrypted
    
    return cipher_dict