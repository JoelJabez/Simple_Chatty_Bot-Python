def main():
    print("Hello! My name is Aid.")
    print("I was created in 2023.")

    name = get_name("Please, remind me your name.")
    print(f"What a great name you have, {name}!")

    age = guess_age()
    print(f"Your age is {age}; that's a good age to start programming")


def get_name(text):
    print(text)
    return input()


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    remainder_of_3 = int(input())
    remainder_of_5 = int(input())
    remainder_of_7 = int(input())

    sum = (remainder_of_3 * 70) + (remainder_of_5 * 21) + (remainder_of_7 * 15)
    actual_age = sum % 105

    return actual_age


main()
