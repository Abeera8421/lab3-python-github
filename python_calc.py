def add(a, b): 

    return a + b 

  

  

def subtract(a, b): 

    return a - b 

  

  

def multiply(a, b): 

    return a * b 

  

  

def divide(a, b): 

    if b == 0: 

        return None  # signals division by zero 

    return a / b 

  

  

def check_even_odd(n): 

    if n % 2 == 0: 

        return "even" 

    else: 

        return "odd" 

  

  

def percentage(a, b): 

    # Return a as a percentage of b. 

    if b == 0: 

        return None 

    return (a / b) * 100 

  

  

def get_number(prompt): 

    # Keep asking until the user enters a valid number. 

    while True: 

        try: 

            return float(input(prompt)) 

        except ValueError: 

            print("Invalid input. Please enter a number.") 

  

  

def get_two_numbers(): 

    return get_number("Enter first number: "), get_number("Enter second number: ") 

  

  

def show_menu(): 

    print("\n===== Python Calculator =====") 

    print("1. Addition") 

    print("2. Subtraction") 

    print("3. Multiplication") 

    print("4. Division") 

    print("5. Check Even/Odd") 

    print("6. Calculate Percentage") 

    print("7. Exit") 

  

  

def main(): 

    while True: 

        show_menu() 

        choice = input("Choose an option (1-7): ").strip() 

  

        if choice == "7": 

            print("Goodbye!") 

            break 

  

        if choice not in {"1", "2", "3", "4", "5", "6"}: 

            print("Invalid choice. Please select 1-7.") 

            continue 

  

        a, b = get_two_numbers() 

  

        if choice == "1": 

            print(a, "+", b, "=", add(a, b)) 

        elif choice == "2": 

            print(a, "-", b, "=", subtract(a, b)) 

        elif choice == "3": 

            print(a, "x", b, "=", multiply(a, b)) 

        elif choice == "4": 

            result = divide(a, b) 

            if result is None: 

                print("Error: This is undefined as the denominator is zero.") 

            else: 

                print(a, "/", b, "=", result) 

        elif choice == "5": 

            print(a, "is", check_even_odd(a) + ".") 

            print(b, "is", check_even_odd(b) + ".") 

        elif choice == "6": 

            result = percentage(a, b) 

            if result is None: 

                print("Error: Cannot calculate percentage of zero.") 

            else: 

                print(a, "is", str(round(result, 2)) + "% of", b) 

  

main() 
