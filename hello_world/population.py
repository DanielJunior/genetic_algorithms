from hello_world import chromosome as chr


class Population():
    MAX_GENERATION = 1000

    def __init__(self, goal, size):
        self.members = []
        self.goal = goal
        self.size = size
        self.generation_number = 0
        self.populate()

    def populate(self):
        tmp = self.size
        while (tmp > 0):
            chromosome = chr.Chromosome()
            chromosome.random(len(self.goal))
            self.members.append(chromosome)
            tmp -= 1

    def sort(self):
        self.members = sorted(self.members, key=lambda member: member.cost)

    def display(self):
        print("Generation: " + str(self.generation_number))
        print("Members:")
        for member in self.members:
            print(member.code + " - " + str(member.cost))

    def generation(self):
        for member in self.members:
            member.calcCost(self.goal)

        self.sort()
        self.display()
        selecteds = self.crossover_selection()
        children = selecteds[0].crossover(selecteds[1])
        self.natural_selection(children)

        for member in self.members:
            member.mutate()
            member.calcCost(self.goal)
            if (self.stop(member)):
                self.sort()
                self.display()
                return True
        self.generation_number += 1
        return False

    def crossover_selection(self):
        return self.members[:2]

    def natural_selection(self, children):
        self.members.pop(len(self.members) - 1)
        self.members.pop(len(self.members) - 2)
        self.members = self.members + children

    def stop(self, member):
        if member.code == self.goal:
            return True
        return False

    def start(self):
        found = False
        while self.generation_number < Population.MAX_GENERATION and not found:
            found = self.generation()
