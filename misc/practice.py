class Apple:
    def add(self, a, b):
        assert a > 10 and b > 10, "a and b should be both greater than 10!"
        return a + b

a = Apple()
# a.run() # AttributeError
# a.add(9, 10) # AssertionError
# a in Apple # SyntaxError


# def func()
#     print("Hello")

# func() # Syntax error

# print("a" + 10) # TypeError

# lis = [1, 2, 3]
# print(lis[3]) # IndexError

# def do_something():
#     x = 10

# print(x) # NameError

# def recur():
#     recur()

# recur() # RecursionError

# def hello():
# print("Hello")

# hello() # Indentation Error

# import math
# print(math.sqrt(-10)) # ValueError