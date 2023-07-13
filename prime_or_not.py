def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

print (f"The output is: {number}" )