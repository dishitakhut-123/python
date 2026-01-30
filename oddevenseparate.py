#ask the use to enter the number
#separate even and odd numbers in separate list till input number 
num=int(input("Enter a number:"))
odd =[]
even=[]
for i in range (1,num+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers ",even)
print("odd numbers ",odd)