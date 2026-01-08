age= int(input("Enter your age"))
if age<12:
    print("Kid")
elif age<20 and age >12:
    print("Teen")
elif age >20 and age <60:
    print("adult")
else:
    print("Senior citizen")