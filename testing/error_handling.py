import logging
def try_something():
    try:
        a = 1
        b = 0

        # if b == 0:
        #     raise ValueError("Cannot divide by 0!")
        print(a / b)
    except Exception as e:
        logging.error(e)
    else:
        print("No errors were found!")
    finally:
        # return
        print("Exiting the error handling!")

    print("Hello")

try_something()