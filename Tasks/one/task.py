# task one => write a pyton program for caulculating tha sum first 10 natural Numbers using loops ?

sum = 0

for i in range(1,11):
#    print(i)
    
    sum +=i
    
    
# print(sum)


    # task no 2 => write a Program for the count Number of digits ,alphabets and spcecial caharacter in a string.

# Take input from user
# text = input("Enter a string: ")

# Initialize counters
# digits = 0
# alphabets = 0
# special_chars = 0

# Loop through each character in the string
# for char in text:
#     if char.isdigit():  # this is new for me like isdigit()
#         digits += 1
#     elif char.isalpha(): # also this isalpha()
#         alphabets += 1
#     else:
#         special_chars += 1

# Display the results
# print("Number of digits:", digits)
# print("Number of alphabets:", alphabets)
# print("Number of special characters:", special_chars)



# task no 3 => write a python program for find out min and max form an list using loop.


# list = [12,34,45,56,33,66,87]

# min = list[0]

# max = list[0]

# for num in list:
#     if num < min:
#         min = num
#     if num >= max:
#         max = num
    
# print("Minimum number is:", min)
# print("Maximum number is:", max)



# task no 4 => write a python program for perform Bubble Sort of a list.

# numbers = [3,5,6,9,2,4,6,7]

# n = len(numbers)

# for i in range(len(numbers)):
#     for j in range(len(numbers)-1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j],numbers[j+1] = numbers[j + 1],numbers[j]

# # i can't under stend but steel 
# print("shorted list ", numbers)





# task no 5 =>  write a python program for calculating of factorial of given numbers.

# num = int(input("enter the number"))

# factorial = 1

# for i in range(1,num+1):
#     factorial = factorial * i

# print("factorial si ", factorial)



# patterns in Python 
# 1
# for i in range(1,4):
#     for j in range(i):
#         print("*" ,end= "")
#     print()
    
# 2
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j , end= "")
#     print()

#3 

# for i in range(1,4):
#     for j in range(i):
#         print(i,end="")
#     print()


#4
# for i in range(3, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
