#WAP to ask the userto entered name of their 3 faborite movies & store  them  in a list

movies =[]
A= input("Enter the first movie :")
B= input("Enter the second movie :")
C= input("Enter the third movie :")
movies.append(A)
movies.append(B)
movies.append(C)
print(movies)

#WAP to check if a list contain a palindrom of element 

list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("Palindrom")
else:
    print("not a Palindrom")    
