with open("python.txt",'r', encoding="utf-8") as file:
	try:
		res = [line.strip() for line in file.readlines()]
		print(res)
		print("Read line ok")
	except FileNotFoundError:
		print("Readline error, file does not exist.")
