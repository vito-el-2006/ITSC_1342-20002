while True:
	name = input("Who are you?").strip("\n")
	if name != "Joe":
		continue
	password = input("Hello, Joe. What is the password? (It is a fish.)").strip("\n")
	if password == "swordfish":
		break
print("Access granted.")
