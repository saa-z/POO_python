"""We are first interested in the representation of an engine. The technical manager
 of the F1 team explains the following:
 • an engine is defined by its fuel (which can be either petrol or diesel) and
 its power (in hp);
 • the engines he works with always have a power greater than 600 hp;
 • by default, the engines will be considered petrol engines with the minimum power;
it is possible to change the power of an engine but absolutely impossible to
 change its fuel."""


class Engine:
    def __init__(self, fuel='petrole', power=600):
        self.__fuel = fuel
        self.power = max(600,power)

    def __str__(self):
        return "Engine {Fuel: " + self.__fuel + " ; Power: " + str(self.power) + " }"

    def change_power(self, new_Power):
        if new_Power > 600:
            self.power = new_Power

#Test 1 : vérification de la définition de notre classe Engine
engine1 = Engine("diesel",540)
print(engine1)
engine1.change_power(540)
print(engine1)
engine1.power=540
print(engine1)

"""Now that we are able to create engines,we are going to start working on cars.
 The head of the Formula1 team’s fleet explains the following:
 •each car is defined by a registration number,a brand,and of course a single
 engine;
 •the registration number has to unique (two different cars cannot have the same number)and has to be generated automatically when creating a new
 car;
 • it is not possible to change nor the registration number neither the brand of acar;
 •however, it is possible to replace its engine."""

class Formula1:
    _next_registration_number = 1
    def __init__(self, registration_number,brand,engine):
        self.__registration_number = Formula1._next_registration_number
        Formula1._next_registration_number+=1
        self.__brand=brand
        self.engine=engine


