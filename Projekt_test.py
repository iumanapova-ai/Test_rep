class Summ_digit:

    def __init__(self, one_digit, two_digit):
        self.one_digit = one_digit
        self.two_digit = two_digit

    def summ_digit(self):
        summ = self.one_digit + self.two_digit
        print(summ)


Summ_digit(1, 2).summ_digit()

