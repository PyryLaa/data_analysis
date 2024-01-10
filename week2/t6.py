'''
This is a class for a fraction number
class contains a simplify method
that will simplify the fraction 
using the greatest common divisor method
and Euclidean algorithm
'''


class fraction:
    numerator = None
    denominator = None
    
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den 
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
    def simplify(self):
        a = self.numerator
        b = self.denominator
        
        while b != 0:
            temp = b
            b = a % b
            a = temp
        
        self.numerator = int(self.numerator / a)
        self.denominator = int(self.denominator / a)
            

f1 = fraction(34562, 311058)

print(f1)
f1.simplify()
print(f1)



