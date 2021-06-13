from functools import reduce

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, filter(lambda num: num % 2 == 0, domain))
# print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
# print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain)
# print(the_sum)


class User:
    active_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def activate(self):
        if self.is_active():
            self.__class__.active_users.append(self.name)

    def deactivate(self):
        if not (self.is_active()):
            self.__class__.active_users.remove(self)

    def is_active(self):
        """
        Check if user is active
        return: Boolean
        """
        return self in self.__class__.active_users


me = User("Brad", "Yeo.bradley@gmail.com")
me.name = "Bradley"
# print(me.name)
# print(me.__dict__)
# # pprint(dir(me))
# User.activate(me)
# print(me.active_users)


# help(User)

class Plant:
    def __init__(self, spec):
        self.spec = spec


class Cactus(Plant):
    pass


basil = Plant("Ocimum basilicum")
opuntia = Cactus("Opuntia vulgaris")


# print(type(opuntia) == Cactus)
# print(isinstance(opuntia, object))
# print(isinstance(opuntia, Plant))
# print(isinstance(basil, Plant))


class Employee:
    def __init__(self, name, salary, hours_per_week=40):
        self.name = name
        self._salary = hours_per_week
        self._salary = salary
        self.__set_hourly_rate()

    @property  # make this getter
    def hours_per_week(self):
        return self._salary

    @hours_per_week.setter
    def hours_per_week(self, value):
        self._salary = value
        self.__set_hourly_rate()

    @hours_per_week.deleter
    def hours_per_week(self):
        del self._salary

    def __set_hourly_rate(self):
        self._hourly_rate = round(self._salary / 52 / self._salary, 2)

    @property  # make this getter
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
        self.__set_hourly_rate()

    @salary.deleter
    def salary(self):
        del self._salary
    
e = Employee("brad", 2000, 5)
# print(e._salary)
e.salary = 11000
# print(e.salary)

def add_four(func):
    def wrapper_func(*args,**kwargs):
        print('Adding 4')
        result = func(*args, **kwargs)
        return result + 7

    return wrapper_func

def Double(func):
    def wrapper_func(*args,**kwargs):
        print('Double')
        result = func(*args, **kwargs)
        return result * 2
    return wrapper_func

@Double
@add_four
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

print(add(1, 3))