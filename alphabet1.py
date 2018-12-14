while True:
	print("Enter '0' for exit.")
	ch = input("Enter any character: ")
	if ch == '0':
		break
	else:
	if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
			print("the given character",ch, "is an alphabet.\n")
	else:
			print("the given chracter",ch, "is not an alphabet.\n")
