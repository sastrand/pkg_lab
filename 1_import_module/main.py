# import the hello and bye functions from the salutations module
# with the import syntax to make this code run

from salutations import hello, bye


def get_name():
    return input("Please enter your name.\n")


def greeter(name):
    print(hello(name))
    print("and")
    print(bye(name))


if __name__ == "__main__":
    n = get_name()
    greeter(n)
