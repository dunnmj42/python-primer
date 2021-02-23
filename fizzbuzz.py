# Basic stuff here:

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif num % 3 == 0:
#         print("fizz")
#         continue
#     elif num % 5 == 0:
#         print("buzz")
#         continue
#     else:
#         print(num)
        
# BIG BRAIN MOVES - shoutout Ben Awad and Konstantin Farrell

for i in range(1, 101): print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))