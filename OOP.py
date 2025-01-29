'''
OOP en Python.
'''


class Car:
    def __init__(self, model: str, kms: int):
        self.model = model
        self.kms = kms

    def __repr__(self):
        return f'Modelo: {self.model} | KM: {self.kms}'

    def broom(self, distance: int):
        self.kms += distance


daily = Car('Porsche 911', 0)
print(daily)
daily.broom(50)
print(daily)