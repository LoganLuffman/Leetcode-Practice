def fizzbuzz(num):
    ans = []
    for n in range(1, num+1):
        if n % 5 == 0 and n % 3 == 0:
            ans.append("FizzBuzz")
        elif n % 5 == 0:
            ans.append("Buzz")
        elif n % 3 == 0:
            ans.append("Fizz")
        else:
            ans.append(n)
    return ans

print(fizzbuzz(30))