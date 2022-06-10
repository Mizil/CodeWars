#1.Write a method, that will get an integer array as parameter and will process every number from this array.
#Return a new array with processing every number of the input-array like this:
#If the number has an integer square root, take this, otherwise square the number.


import math
def square_or_square_root(arr):
    for item in range(len(arr)):
        if math.sqrt(arr[item]) % 1 == 0:
           arr[item] = int(math.sqrt(arr[item]))
        else:
            arr[item] = arr[item] * arr[item]

    print(arr)

#square_or_square_root([3,4,9,2])

print(math.sqrt(3))

#2.Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    suma = 0
    for item in range(len(numbers)):
        suma = suma + numbers[item] * numbers[item]

    print(suma)

#square_sum([1,2,2])

#3.Create a function that returns the CSV representation of a two-dimensional numeric array.
from array import *
def to_csv_text(array):
    new_string = ""
    for rows in range(len(array)):
        for cols in range(len(array[rows])):
            print(array[rows][cols] , end = ' ' )
        print("\n")



array = [[ 0, 1, 2, 3, 4 ], [ 10,11,12,13,14 ], [ 20,21,22,23,24 ], [ 30,31,32,33,34 ]]
print (array[0])
#to_csv_text(array)


#4.Write a function that returns a string in which firstname is swapped with last name.
#def name_shuffler(str_):
nume = "ala bala"
nume1 = nume.split(" ")

for i in range(int(len(nume1)-1)):
    a = nume1[i]
    nume1[i] = str(nume1[i+1])
    b = str(a)
    new_string = nume1[i] + " " + b

print (new_string)


#5.We want to know the index of the vowels in a given word, for example, there are two vowels
# in the word super (the second and fourth letters).

#So given a string "super", we should return a list of [2, 4].
def vowel_indices(word):
    lista=[]
    word.lower()
    for i in range(len(word)):
        if word[i] in "aeiou":
            lista.append(i+1)
    print(lista)
vowel_indices("UNDISARMED")
word = "UNDISARMED"
#print(word.lower())



#6.Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
def remove_every_other(my_list):
    new_list=[]
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(my_list[i])

    print(new_list)

#remove_every_other(["Keep", "Remove","Keep", "Remove","Keep", "Remove","Keep", "Remove"])

#7.Simple, remove the spaces from the string, then return the resultant string
def no_space(x):
    new_str = ""
    for c in range(len(x)) :
        if x[c] != " ":
            new_str = new_str + x[c]

    print(new_str)
no_space("aa b b")





