count = 0
pre = count
sum = []
while count >= 0:
    a = int(input("Enter a Number: "))
    sum.append(a)
    pre = count
    count += a
print("Program exit")
sum.pop()
print("The numbers before which sum becomes negative are", sum)