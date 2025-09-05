import time

print("Hello User!") 

print("*" * 10)

print("What is your name?")

name = input("Enter your name:") # input makes it so that the user can interact

print(f"Hello {name}, what can I do for you today?")

time.sleep(1)

print("1. Calculate")

time.sleep(1)

print("2. Tell the time")

time.sleep(1)

print("3. Tell me a joke")

time.sleep(1)

print("4. Countdown for me")

choice = input("Input:")

if choice == "1":
    num1 = float(input("First number:"))
    op = input("Operation? (-, x, +, /):")
    num2 = float(input("Second number:"))
    if op == "x":
        result = num1 * num2
    if op == "-":
        result = num1 - num2
    if op == "+":
        result = num1 + num2
    if op == "/":
        result = num1 / num2
    print(result)

elif choice == "2":
    print(time.strftime("%H:%M:%S"))

elif choice == "3":
    print("Knock knock?")
    reply = input("").strip().lower()
    if reply == ("who's there?"):
        print("Why are you even asking? Im a terminal asistant, not your mailman! XD")
    else:
        print("You're supposed to say 'who's there?'")

elif choice == "4":
    a = int(input("First number:"))
    b = int(input("Ending number:"))
    while a <= b:
        print(a)
        time.sleep(1)
        a = a + 1
        print("Done!")







































