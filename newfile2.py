import datetime
import os
import platform
import random
import sys
import webbrowser

def pyos_shell():
    print("Welcome to PyOS Shell. Type 'help' for a list of commands.")

    while True:
        cmd = input("PyOS> ").strip().lower()

        if cmd == "exit":
            print("Exiting PyOS Shell...")
            break
        elif cmd == "help":
            print("Available commands:")
            print("  help        - Show this help message")
            print("  exit        - Exit the shell")
            print("  time        - Show current system time")
            print("  os          - Show operating system info")
            print("  clear       - Clear the screen")
            print("  echo        - Repeat your input")
            print("  randint     - Generate a random number")
            print("  pythonver   - Show Python version")
            print("  date        - Show current date")
            print("  browser     - Open a website in your browser")
            print("  calc        - Simple calculator (add, sub, mul, div)")
        elif cmd == "time":
            print("Current time:", datetime.datetime.now().strftime("%H:%M:%S"))
        elif cmd == "date":
            print("Current date:", datetime.date.today())
        elif cmd == "os":
            print("OS Name:", os.name)
            print("Platform:", platform.system(), platform.release())
        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == "echo":
            text = input("Enter text to echo: ")
            print(text)
        elif cmd == "randint":
            print("Random number:", random.randint(1, 100))
        elif cmd == "pythonver":
            print("Python version:", sys.version)
        elif cmd == "browser":
            url = input("Enter URL to open (include http:// or https://): ")
            webbrowser.open(url)
        elif cmd == "calc":
            try:
                a = float(input("Enter first number: "))
                op = input("Enter operation (+, -, *, /): ")
                b = float(input("Enter second number: "))
                if op == '+':
                    print("Result:", a + b)
                elif op == '-':
                    print("Result:", a - b)
                elif op == '*':
                    print("Result:", a * b)
                elif op == '/':
                    if b != 0:
                        print("Result:", a / b)
                    else:
                        print("Error: Division by zero.")
                else:
                    print("Unknown operator.")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        else:
            print(f"Unknown command: {cmd}")

# Run the shell
pyos_shell()