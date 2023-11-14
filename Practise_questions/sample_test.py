from sample import *

assert(exchange_val(100,20)==(20,100))

assert(positive(1))

assert(divisibleNum(20,4)==[4,8,12,16,20])

assert(oddNum(10)==[1,3,5,7,9])

assert(quo_rem(5,4)==(1,1))

#assert(sumofdigit(123)==6)

assert(smallestDivisor(10)==2)

assert(compute(2)==14)

assert(reverse(1234)=='4321')

assert(average([1,2,3])==2)

assert(count(123)== 3)

assert(palindrome(1234)== 4321)

assert(no_of_occurnce('abcdabcsabcdabcs','a')==(4))



assert( point_of_occurance('sample string ','str')==(7))
assert( point_of_occurance('sample string ','abc')==(-1))


assert(all_alphabets('thiscontainsallalphabets'))

assert(replace_substring('ababa','a','$')==('$b$b$'))

assert(no_of_vowels('This sentece is used to check assertion for number of vowels in a string')==(22))


assert(replace('this is sample to understand')==('this-is-sample-to-understand'))


assert(larger('first string','second string')==('second string'))