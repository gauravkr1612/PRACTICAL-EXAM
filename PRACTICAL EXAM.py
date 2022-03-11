#QUESTION 1
#(a) sum of first n odd no.

n=int(input('how many odd no. sum: '))
odd=1
sum=0
for i in range(n):
    sum+=odd
    odd+=2
print('the sum of first',n,'odd no. is',sum)

OUTPUT:  ==========
how many odd no. sum: 5
the sum of first 5 odd no. is 25
    

#(b) sum of first n even no.

n=int(input('how many even no. sum: '))
even=0 # 0 is also an even no.
sum=0
for i in range(n):
    sum+=even
    even+=2
print('the sum of first',n,'even no. is',sum)

OUTPUT:
how many even no. sum: 4
the sum of first 4 even no. is 12
    


 #(c) sum of series given... which seems like 




#QUESTION 2
# t1=(1,2,5,7,9,2,4,6,8,10)

#(a)
t1=(1,2,5,7,9,2,4,6,8,10)
t2=t1[:5]
t3=t1[5:]
print(t2)
print(t3)

Output:  
(1, 2, 5, 7, 9)
(2, 4, 6, 8, 10)

#(b)

t1=(1,2,5,7,9,2,4,6,8,10)
n=list(t1)
l1=list()
for i in n:
    if i%2==0:
            l1.append(i)
    p=tuple(l1)
print('the original tupple: ',t1)
print('tuple with even element is:',p)

#OUTPUT:
  the original tupple:  (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
tuple with even element is: (2, 2, 4, 6, 8, 10)
  
  
  #(c)
  
t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
t3=t1+t2
print('t1: ',t1)
print('t2: ',t2)
print('the contatinated, t3: ',t3)

OUTPUT:
t1:  (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2:  (11, 13, 15)
the contatinated, t3:  (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
  
  #(d)
  
 t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print('max no. is',max(t1))
print('min no. is',min(t1))

OUTPUT:
max no. is 10
min no. is 1




#QUESTION 3 MENU DRIVEN PROGRAM

def string():
    choice =input('''Enter your choice 
a = length of the string
b = maximum of three strings
c = Replace every successive character with #
d = number of words in the string
enter: ''')

    if choice =='a':
        n = input("Enter a string : ")
        lgth=len(n)
        print("The length of the string is =",lgth)      
    elif choice == 'b':
        n1 = input("Enter 1st string : ")
        n2 = input("Enter 2nd string : ")
        n3 = input("Enter 3rd string : ")
        print("The maximum of the three strings is =",max(n1,n2,n3))    
    elif choice == 'c':
        n = input("Enter a string : ")
        s = ""
        m = list(n)
        for i in range(len(n)):
            if (i%2 != 0):
                if m[i] == " ":
                    m[i] = " "
                else:
                    m[i] = "#"
        for x in m:
            s=s+x
        print("The sucessive character in the string is replaced with # :",s) 
    elif choice == 'd':
            n = input("Enter a string : ")
            c = 0
            for y in n :
                if y == " " :
                    c += 1
            w = c+1
            print("The number of words = ",w) 
    else :
        print("this was not the desired input!!!!!")

string()
