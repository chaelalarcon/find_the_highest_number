# define 5 variables
# compare var1 to var2, var3, var4 and var5
# if var1 > var2 and var1 > var3 and var1 > var4 and var1 > var5:
   # print var1 as the highest number
# compare var2 to var1, var3, var4 and var5
# elif var2 > var1 and var2 > var3 and var2 > var4 and var2 > var5:
   # print var2 as the highest number
# compare var3 to var1, var2, var4 and var5
# elif var3 > var1 and var3 > var2 and var3 > var4 and var3 > var5:
   # print var3 as the highest number
# compare var4 to var1, var2, var3 and var5
# elif var4 > var1 and var4 > var2 and var4 > var3 and var4 > var5:
   # print var4 as the highest number

# if not:
   # print var5 as the highest number


first = int(input("Enter 1st number: "))
second = int(input("Enter 2nd number: "))
third = int(input("Enter 3rd number: "))
fourth = int(input("Enter 4th number: "))
fifth = int(input("Enter 5th number: "))

if first > second and first > third and first > fourth and first > fifth:
    print("First number is the highest number")
elif second > first and second > third and second > fourth and second > fifth:
    print("Second number is the highest number")
elif third > first and third > second and third > fourth and third > fifth:
    print("Third number is the highest number")
elif fourth > first and fourth > second and fourth > third and fourth > fifth:
    print("Fourth number is the highest number")

else:
    print("Fifth number is the highest number")