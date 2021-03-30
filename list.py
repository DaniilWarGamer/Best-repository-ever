class List:
    def __init__(self, lst=[]):
        self.lst =lst
    def __add__(self, other):
        result = []
        for i in range(max(len(self.lst), ))