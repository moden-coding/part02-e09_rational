#!/usr/bin/env python3

from operator import truediv


class Rational(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __add__(self, rat2):
        num1 = rat2.num2*self.num1
        denom1 = self.num2 * rat2.num2
        num2 = rat2.num1 * self.num2
        
        numerator = num1 + num2 
        temp = Rational(numerator, denom1)
        return temp
    
    def __sub__(self, rat2):
        self_rationalized, other_rationalized = self.common_denom(rat2)
        temp = Rational(self_rationalized.num1 - other_rationalized.num1, self_rationalized.num2)
        return temp
    
    def __mul__(self, rat2):
        num = self.num1*rat2.num1
        denom = self.num2 * rat2.num2
        temp = Rational(num, denom)
        return temp
        
    def __truediv__(self, rat2):
        num = self.num1 * rat2.num2
        denom = self.num2 * rat2.num1
        temp = Rational(num, denom)
        return temp
    
    def __str__(self):
        return f"{self.num1}/{self.num2}"
    
    def __eq__(self, other):
        self_rationalized, other_rationalized = self.common_denom(other)
        
        if(self_rationalized.num1 == other_rationalized.num1 and self_rationalized.num2 == other_rationalized.num2):
            return True
        else:
            return False
    def __gt__(self, other):
        self_rationalized, other_rationalized = self.common_denom(other)
        if self_rationalized.num1 > other_rationalized.num1:
            return True
        return False
    
    def __le__(self, other):
        # self_rationalized, other_rationalized = self.common_denom(other)
        # if self_rationalized.num1 > other_rationalized.num1:
        #     return False
        # return True
    
        return not (self > other)
    
    def common_denom(self, other):
        num1 = other.num2*self.num1
        denom1 = self.num2 * other.num2
        num2 = other.num1 * self.num2
        
        new_self = Rational(num1, denom1)
        new_other = Rational(num2, denom1)
        
        return new_self, new_other
        
        
        

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
