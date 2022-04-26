# Determinar los numeros primos del 1 al 100

# from unittest import case


# num = 1

# while(num < 100):
#     div = num % 2
#     div2 = num % num
#     if div == 0 and div2 == 0:
#         print(num)
#     else:
#         print("/")
#     num = num + 1

nums = []


for i in range(1,100,2):
    nums.append(i)
print(nums)
    

