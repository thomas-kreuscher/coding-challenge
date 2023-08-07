"""Task: Prime number generator
Write a Python function that takes a list of prime numbers
generates and returns up to a given limit n. One
Prime number is a natural number greater than 1 that can only be divided by 1
and is divisible to itself. Expected output using n=20: [2, 3, 5, 7, 11, 13, 17, 19]"""



def prime_numbers(limit):
    prime_list = [2]
    for i in range(2,limit):
        
        # print(i)
        # if (i % 2 == 0) or ((i > 3) % 3 == 0) or ((i > 5) % 5 == 0):

        if (i % 2 == 0):
            pass
        elif (i > 3) and (i % 3 == 0):
            pass
        elif (i > 5) and (i % 5 == 0):
            pass
        else:
            prime_list.append(i)
            
        
    return prime_list    


print(prime_numbers(20))