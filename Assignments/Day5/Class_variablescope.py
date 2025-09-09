def outer():
    y = 20  # enclosing variable

    def inner():
        x = 10  # local variable
        print("Inner function:", x)
        print("Enclosing variable:", y)

    inner()


outer()
# print("Outer function:", x)  # x is not defined here, will raise an

d = 30  # gloal variable


def func():
    # global d
    # d += 10
    print("Global variable:", d)


func()
print("Global variable outside function:", d)
