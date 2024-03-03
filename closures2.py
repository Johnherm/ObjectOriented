def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function 
# outer_function("Hi")
# outer_function("Bye")
hi_function = outer_function("Hi")
bye_function = outer_function("Bye")
hi_function()
bye_function()