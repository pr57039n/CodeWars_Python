#If the number is divisble by both 3 and 5, it will give fizzbuzz otherwise it'd only give fizz, buzz, or the number as a string.

def fizzbuzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:  
        return "Fizz Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
