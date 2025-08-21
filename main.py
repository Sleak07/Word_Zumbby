def main(a: int, b: int) -> int:
    """
    It's a simple addition sum to test against it's own test case

    Args:
        a(int): The first number.
        b(int): The second number.

    Returns:
        The sum of 'a' and 'b'

    """
    return a + b


if __name__ == "__main__":
    """
    Example usage when running the module directly 
    Prompts user for input and print their sum
    """
    a = int(input("Enter your first number : "))
    b = int(input("Enter your second number : "))
    print(f"The sum is: {main(a, b)}")
    main()
