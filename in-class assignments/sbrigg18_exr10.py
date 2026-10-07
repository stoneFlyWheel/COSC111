def is_prime(n):
    divisor = 2

    # handling the special cases!
    if n == 2 or n == 1:
        return True

    while divisor < n:
        if n % divisor == 0:
            break
        divisor += 1

    if divisor == n: # is prime
        return True
    else: # is not prime
        return False
    
# No need to change the code below this line
n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime!")
else:
   print("Not prime.") 