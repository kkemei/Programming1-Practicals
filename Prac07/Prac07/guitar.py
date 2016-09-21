def get_age(self, year):
    self.age = 2016 - self.year
    return self.age


def is_vintage(self):
    if self.age >= 50:
        self.vintage = True
    else:
        self.vintage = False
    return self.vintage

class Guitar:
    def __init__(self, name="", year=0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = get_age(self, year)
        self.vintage = is_vintage(self)



    def __str__(self):
        # return "{} ({}), Worth ${} | ({}) {}".format(self.name, self.year, self.cost, self.vintage, self.age)
        return "{:>15} ({}), worth ${:10,.2f} {} {}".format(self.name, self.year, self.cost, self.vintage, self.age)

