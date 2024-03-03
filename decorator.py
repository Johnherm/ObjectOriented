def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function
@decorator_function  # = decorated_display = decorator_function(display)
def display():
    print("display function ran ")
display()

