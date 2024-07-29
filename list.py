marks = [94.5 , 85.5 , 90.5 , 89.5 , 88.5]
print("Marks:", marks)
print(len(marks))
print(type(marks))
print(marks[0])


student =[ "Ansh" ,90.5, "Sanskriti"]
print("Student:", student)
print(student[2])

# strings are immutable(we cannot change the values of string)
# but list are mutable(we can change the values of list)

str = "Hello"
print(str[0])

# list slicing  [start:stop:step]  start is inclusive and stop is exclusive



marks = [94 , 85 , 90 , 89 , 88]
print(marks[:-4])


# append()  add the element at the end of the list

list =[2, 1,3 ,4]
list.append(5)
print(list)


# sort the list in ascending order  sort()  method  

list =[2, 1, 3 ,4]
print(list.sort(reverse=True)) 
print(list.append(0))
print(list)

list =['a', 'c', 'b', 'f', 'e']

print(list.sort())
print((list))



list =['a', 'c', 'b', 'f', 'e']     
print(list.reverse())
print(list)


list =['car', 'bike', 'bus', 'train']
print(list.insert(2, 'aeroplane'))
print(list)


list =[6, 7, 8, 9]
list.pop(3)
print(list)


#  tuple is immutable   list is mutable

#  tuple is defined by ()  and list is defined by []

#  tuple is faster than list

#  tuple is used for read only purpose

#  tuple is used for fixed data

tup = (1, 2, 3, 4, 5)
print(tup)  
print(type(tup)) 


tup = (1, 2, 3, 4, 5)
print(tup[0])



# tuple methods count()  and index() are used to count the number of elements in the tuple and to find the index of the element in the tuple

tup.index(3)  # find the index of the element in the tuple

tup.count(3) # count the number of elements in the tuple



movies =[]

mov = input ('Enter 1st movie:') 
movies.append(mov)
mov = input ('Enter 2nd movie:')
movies.append(mov)
mov = input ('Enter 3rd movie:')
movies.append(mov)
mov = input ('Enter 4th movie:')
movies.append(mov) 
print(movies)
    
    
    
movies =[]

movies.append(input ('Enter 1st movie:'))
movies.append(input ('Enter 2nd movie:'))
movies.append(input ('Enter 3rd movie:'))

print(movies)



# palindrome program   (string is palindrome or not)    

#  string is palindrome if it is same as the reverse of the string

#  example:  madam, radar, level, refer, rotator, deed,
# civic, noon, racecar, redder, repaper, 
# reviver, rotator, sagas, solos, stats, tenet, wow



list =[1,2,1]
list2 =[1,2,3]

copy_list = list.copy()
copy_list.reverse()


if(copy_list == list):
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
    
Number = ('c', 'i', 'v', 'p', 'c')
print(Number.count('i'))