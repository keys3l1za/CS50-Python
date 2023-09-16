u_greeting = input("Greeting: ").strip().lower()

if u_greeting.startswith("hello"):
    cost = "$0"
elif u_greeting.startswith("h"):
    cost = "$20"
else:
    cost = "$100"

print(f"{cost}")
