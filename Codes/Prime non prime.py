def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime No.")
    else:
        print("Its not a prime no.")

n = int(input("Check this number: "))
prime_checker(number=n)
