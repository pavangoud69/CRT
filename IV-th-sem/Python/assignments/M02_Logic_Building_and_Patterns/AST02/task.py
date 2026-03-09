def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
        
    return sign * rev

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))