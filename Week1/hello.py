print("Hello, world!")
name = input("What is your name?\n").strip("\n")
print(f"Nice to meet you {name}")
print(f"The length of your name is:\n{len(name)}")
age = 0
while True:
	try:
		age = int(input("What is your age?\n").strip("\n"))
		if age <= 0:
			print("Input an age greater than 0.")
		else:
			break
	except ValueError:
		print("Please input a whole numerical value.")
print(f"You will be {age + 1} in a year.")
