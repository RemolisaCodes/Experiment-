# this is the final test program assigned by Eng.Eman Bishr

arr=[] # AN EMPTY VARIABLE

# To let the user insert the number of items in the list 'arr' and save the number in the variable "n"
while True:
        n=int(input("Enter the number of items: "))
        if n>0: # To check if the inserted number is possitive
            break
for i in range(n): # a loop to let the user assign the items values
    while True:# a loop to handle exception if the user didn't assign an integer
        try:
            items=int(input ("Enter an integer item, please:\n"))
        except:
            print("invalid ")
        else:
            arr.append(items)
            break

# showing outputs of the number if possitive,negative,and zero values
pos=[]
neg=[]
zero=[]
for i in arr:
    if i > 0 :
        pos.append(i)
    elif i < 0 :
        neg.append(i)
    else:
        zero.append(i)    

print(f"The number of possitive numbers is: {len(pos)}")
print(f"The number of negative numbers is: {len(neg)}")
print(f"The number of zeroes is: {len(zero)}")

#turning possitives and negatives
posNegOnes=[]
for i in arr:
    if i > 0:
        posNegOnes.append(1) 
    elif i < 0:       
        posNegOnes.append(-1)
    else:
        posNegOnes.append(0)
        
# Showing all lists
print (arr)
print(pos, neg, zero)
print(posNegOnes)
