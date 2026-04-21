name = input("Enter your name: ")
age = input("Enter your age: ")

print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Age: {age}")

if int(age) >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")