from collections import deque

class AnimalShelter:
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()
        self.priority = 0

    def addDog(self):
        self.dogs.append(self.priority)
        self.priority += 1

    def addCat(self):
        self.cats.append(self.priority)
        self.priority += 1

    def removeDog(self):
        return self.dogs.popleft()

    def removeCat(self):
        return self.cats.popleft()

    def removeEither(self):
        if not (self.cats or self.dogs):
            return None
        if not self.cats:
            return self.dogs.popleft()
        if not self.dogs:
            return self.cats.popleft()
        if self.dogs[0] < self.cats[0]:
            return self.dogs.popleft()
        return self.cats.popleft()
