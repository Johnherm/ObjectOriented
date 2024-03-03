def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function
@decorator_function  # = decorated_display = decorator_function(display)
def display():
    print("display function ran ")
display()
@decorator_function
def display_info(name,age):
    print(f"display info ran with arguments {name, age}")
display_info('John',25)


decorated_display = decorator_function(display)
decorated_display()

