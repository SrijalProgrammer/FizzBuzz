def div_by_3(x: int) -> bool:
    """
    # Function
    Function Name: div_by_3
    Function Desc: Check the divisiblity of param x with 3.

    # Params
    x: int
    
    # Output
    True || False: bool
    """
    if int(x) % 3 == 0: return True
    return False

def div_by_5(x: int) -> bool:
    """
    # Function
    Function Name: div_by_5
    Function Desc: Check the divisiblity of param x with 5.

    # Params
    x: int
    
    # Output
    True || False: bool
    """
    if int(x) % 5 == 0: return True
    return False

if __name__ == "__main__":
    print("==FizzBuzz==")
    
    for num in range(1,101):
        result = ""
        if div_by_3(num) and div_by_5(num): result = "Fizz Buzz"
        elif div_by_3(num): result = "Fizz"
        elif div_by_5(num): result = "Buzz"
        else: result = "Neither!"

        print(f"['{num}': '{result}']")

    print("==FizzBuzz==")