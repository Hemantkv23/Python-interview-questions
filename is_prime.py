def is_prime(n):
    for i in range(2, n//2):
        if n%i == 0 :
            return False
    else:
        return True


print(is_prime(8))