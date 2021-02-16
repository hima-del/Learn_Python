def outer_function():
    messgae="hi"

    def inner_function():
        print(messgae)
    return inner_function()

outer_function()        