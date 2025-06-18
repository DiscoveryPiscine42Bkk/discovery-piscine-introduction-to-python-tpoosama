#!/usr/bin/env python3
#รับตัวเลข
num = int(input("Enter a number less than 25\n").strip())
#เช็กว่ามากกว่า 25 ไหม
if num > 25:
    print("Error")
else:
    while num <= 25:
        print("Inside  the loop, my variable is")
        print(num)
        num += 1