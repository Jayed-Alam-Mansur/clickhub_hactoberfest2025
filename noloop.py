def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print(f"Factorial of {N} is {factorial(N)}")
