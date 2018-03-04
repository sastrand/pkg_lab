# import the hello and bye functions from the salutations module
# with the import syntax needed to make this code run

# [add import statment here]

def get_name():
	return input("Please enter your name.\n")

def greeter(name):
	print(salutations.hello(name))
	print("and")
	print(salutations.bye(name))

if __name__ == "__main__":
	n = get_name()
	greeter(n)
