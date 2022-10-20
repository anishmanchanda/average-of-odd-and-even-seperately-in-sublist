#to find average of odd and even numbers seperately

n=int(input("enter number of numbers"))
list=[]
even=[]
odd=[]

for i in range (n):
    num = int(input("enter a number"))
    list.append(num)

    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print(list)
print(even)
print(odd)

sumeven=0
sumodd=0
for i in range(len(even)):
    sumeven=sumeven + even[i]

for i in range(len(odd)):
    sumodd=sumodd + odd[i]

avgeven=sumeven/len(even)    
avgodd=sumodd/len(odd)

print("average of entered even numbers is",avgeven)
print("average of entered odd numbers is",avgodd)
