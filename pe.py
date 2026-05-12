
# x = 1

# while x <= 3:
#     if x == 2:
#         print(x)
#         break
#     x += 1 #Shorthand assignment (Add value of x by 1)
# else:
#     print("Loop finished.")
    
    #1st Iteration
#1.Evaluate the condition using the initial value of (x), if it evaluates to True, block of code will execute (display output of 1st iteration)
#Second Iteration
#1. Using the current value of (x), add the value of x by 1 using the expression (x +=1) 1+1=2
#2. Carry the updated value of the x based on the result of the expression and use it to evaluate the condition. If true, then you can print
# the output.
#3. Repeat 1 and 2. (second iteration)
#4. The program will terminate if while condition became False.

#While loop in Collection
# numbers = [1,2,3,4]
# i = 0 #index position

# while i < len(numbers):
# print(numbers[i])
# i += 1


# i = 1
# while i < 6:
#  print(i)
#  i += 1
# else: 
#     print("Loop finished.")

# loops = 100
# for n in range(loops):
#     print('-'*n, end="")

#One dimensional collection

# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# for row in matrix:
#     for every_item in row:
#         print(every_item, end=" ")
#     print()

# data = [
#     [
#         [1,2,3],
#     ],
#     [
#         [4,5,6],
#     ],
#     [
#         [7,8,9]
#     ]
# ]

# for layers in data:
#     for row in layers:
#         for every_item in row:
#             print(every_item, end="-")
#         print()


for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
   