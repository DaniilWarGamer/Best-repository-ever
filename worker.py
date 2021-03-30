class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def Salary(self):
        return self.rate * self.days
    def __str__(self):
        return f'Worker {self.name} {self.surname} have {self.rate} dollars per day and has already worked for {self.days} days'
    