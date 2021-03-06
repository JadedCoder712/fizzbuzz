"""
fizzbuzz.py
Author: Kyle Postans
Credit: Mr. Dennison

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""

numbers = input("How many numbers shall we print? ")
fizz = input("For multiples of what number shall we print 'Fizz'? ")
buzz = input("For multiples of what number shall we print 'Buzz'? ")

list3 = range(1, 105)
list5 = range(1, 105)

multipleslist3 = [a * int(fizz) for a in list3]
multipleslist5 = [b * int(buzz) for b in list5]

#megamultipleslist = zip(multipleslist3, multipleslist5)

mylist = range(1, int(numbers) + 1)


for x in mylist:
    if x in multipleslist3 and x not in multipleslist5:
        print("Fizz")
    elif x in multipleslist3 and x in multipleslist5:
        print("FizzBuzz")
    elif x not in multipleslist3 and x not in multipleslist5:
        print(x)
    elif x in multipleslist5 and x not in multipleslist3:
        print("Buzz")