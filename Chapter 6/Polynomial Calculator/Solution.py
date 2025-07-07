class variable():
    def __init__(self, coefficient, degree):
        self.coeff = coefficient
        self.deg = degree

class polynomial():
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2

    def add(self):
        if self.var1.coeff == 0 and self.var2.coeff == 0:
            return "0"
        elif self.var1.coeff == 0:
            return f"{self.var2.coeff}x^{self.var2.deg}"
        elif self.var2.coeff == 0:
            return f"{self.var1.coeff}x^{self.var1.deg}"
        elif self.var1.deg == self.var2.deg:
            if self.var1.deg == 0:
                return f"{self.var1.coeff + self.var2.coeff}"
            return f"{self.var1.coeff + self.var2.coeff}x^{self.var1.deg}"
        elif self.var1.deg == 0:
            return f"{self.var1.coeff} + {self.var2.coeff}x^{self.var2.deg}"
        elif self.var2.deg == 0:
            return f"{self.var1.coeff}x^{self.var1.deg} + {self.var2.coeff}"
        else:
            return f"{self.var1.coeff}x^{self.var1.deg} + {self.var2.coeff}x^{self.var2.deg}"
        
    def sub(self):
        if self.var1.coeff == 0 and self.var2.coeff == 0 or self.var1.coeff == self.var2.coeff and self.var1.deg == self.var2.deg:
            return "0"
        elif self.var1.coeff == 0:
            return f"-{self.var2.coeff}x^{self.var2.deg}"
        elif self.var2.coeff == 0:
            return f"{self.var1.coeff}x^{self.var1.deg}"
        elif self.var1.deg == self.var2.deg:
            if self.var1.deg == 0:
                return f"{self.var1.coeff - self.var2.coeff}"
            return f"{self.var1.coeff - self.var2.coeff}x^{self.var1.deg}"
        elif self.var1.deg == 0:
            return f"{self.var1.coeff} - {self.var2.coeff}x^{self.var2.deg}"
        elif self.var2.deg == 0:
            return f"{self.var1.coeff}x^{self.var1.deg} - {self.var2.coeff}"
        else:
            return f"{self.var1.coeff}x^{self.var1.deg} - {self.var2.coeff}x^{self.var2.deg}"
    
    def multiply(self):
        if self.var1.coeff == 0 or self.var2.coeff == 0:
            return "0"
        elif self.var1.deg == 0 and self.var2.deg == 0:
            return f"{self.var1.coeff * self.var2.coeff}"
        elif self.var1.deg == 0:
            return f"{self.var1.coeff * self.var2.coeff}x^{self.var2.deg}"
        elif self.var2.deg == 0:
            return f"{self.var1.coeff * self.var2.coeff}x^{self.var1.deg}"
        else:
            return f"{self.var1.coeff * self.var2.coeff}x^{self.var1.deg + self.var2.deg}" 

# Example Input
var1 = variable(4,2)
var2 = variable(3,1)
p = polynomial(var1,var2)
print(p.multiply())
