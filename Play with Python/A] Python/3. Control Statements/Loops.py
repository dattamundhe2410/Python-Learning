
 
for i in range(11): #0 to 10
 
    print(i) #0 to 10
 
 
for j in range(10,21): 
    print(j) #10 to 20
 
for k in range(10,21,3):
    print(k) 

 
for i in range(1,11):
    print(i)
 
for j in range(11):
    print(j)
 
for k in range(1,10,3):
    print(k)
 
 
# WAP to check the number is even or odd
num = 23
if(num%2==0):
    print("even")
else:
    print("odd")
 

# WAP to print string 5 times
s = 'datta'
for i in range(5): 
    print(s)
 
 
 
# WAP to print the numbers from 1 to 20
i=1
while(i<=20):
    print(i)
    i=i+1
 
"""
Loops:-
- Used to access a range of values
- python doesn't support inc/dec operators
 
 
finite - we can predict the start and end range
       - calculate even numbers from 1 to 20
       - leap years from 2000 to 2020
 
 
infinite - we can't predict the end range
        - reading any data from file system
        - reading data from database
 
for  - finite loop
 
for i in range():
   print(i)

"""
 
for i in range(1,11):
   print(i)
 
 """

while - finite and infinite
 
- top tested loop
- checks the cdn first, if it is true then it will access the values inside the loop
 
finite while loop:-
 
initialization;
while(cdn):
  //statement
  //increment/decrement
 
 """

 
#print the numbers div by both 3 and 5
#from 1 to 50
i=1
while(i<=50):
    if(i%3==0 and i%5==0):
        print(i)
    i=i+1
 
#print the square of numbers from 5 to 1
 

 
# WAP to find the factorial value of a given number
n = 5
fact=1
for i in range(1,n+1): 
    fact=fact*i 
print(fact)
