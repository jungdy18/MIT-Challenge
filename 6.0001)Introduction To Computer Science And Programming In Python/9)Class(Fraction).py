class fraction(object):
    def __init__(self,numerator,denominator):
        assert type(numerator) is int and type(denominator) is int, "numerator or denominator is not integer"
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def __float__(self):
        return self.numerator/self.denominator
    def __add__(self,other):
        new_numerator = self.numerator* other.denominator + self.denominator* other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator,new_denominator)
    def __add__(self,other):
        new_numerator = self.numerator* other.denominator - self.denominator* other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator,new_denominator)
    def inverse(self):
        return fraction(self.denominator,self.numerator)
