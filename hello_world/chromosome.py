import sys
import string
import random


class Chromosome():

    def __init__(self, code="", chance=0.5):
        self.code = code
        self.cost = sys.maxsize
        self.chance = chance

    def random(self, length):
        self.code = ""
        while (length > 0):
            self.code += random.choice(string.ascii_letters)
            length -= 1

    def calcCost(self, compareTo):
        total = 0
        for index, char in enumerate(self.code):
            total += (ord(self.code[index]) - ord(compareTo[index])) ** 2
        self.cost = total

    def crossover(self, other):
        pivot = random.randint(0, len(self.code) - 1)
        child1 = Chromosome(self.code[:pivot] + other.code[pivot:])
        child2 = Chromosome(other.code[:pivot] + self.code[pivot:])
        return [child1, child2]

    def mutate(self):
        if random.random() < self.chance:
            return
        index = random.randint(0, len(self.code) - 1)
        upOrDown = random.random()
        code = list(self.code)
        if upOrDown > 0.5:
            code[index] = chr(ord(self.code[index]) + 1)
        else:
            code[index] = chr(ord(self.code[index]) - 1)
        self.code = ''.join(code)

