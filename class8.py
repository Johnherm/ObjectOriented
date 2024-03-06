class Vehicle: #this variable is class
    def __init__(car, make, model):
        car.make = make
        car.model = model
    def moves(car):
        print("Moves along...")
    def get_make_model(car):
        print(f"I'm {car.make}, {car.model}.")



# the variables of the following are objects
my_car1 = Vehicle('Tesla', 'Model 3')
my_car2= Vehicle('Toyota', 'Lexus')
my_car3 = Vehicle('Cadillac','Escalade')
my_car1.get_make_model()
my_car1.moves()
my_car2.get_make_model()
my_car2.moves()
my_car3.get_make_model()
my_car3.moves()
