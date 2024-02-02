from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, candidate_name, votes):
        pass

class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, votes):
        pass

    @abstractmethod
    def vote(self, candidate_name):
        pass

class Candidate(Subject):
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def vote(self):
        self.votes += 1
        self.notify_observers({self.name: self.votes})

    def notify_observers(self, votes):
        for observer in self._observers:
            observer.update(self.name, votes[self.name])

class Voter(Observer):
    def __init__(self, name):
        self.name = name

    def vote(self, candidate):
        candidate.vote()

    def update(self, candidate_name, votes):
        print(f"Candidate {candidate_name} has been voted {votes} time(s).")

if __name__ == "__main__":
    candidate1 = Candidate("John")
    candidate2 = Candidate("Gabriel")

    voter1 = Voter("Pedro")
    voter2 = Voter("Maria")
    voter3 = Voter("Lucas")
    voter4 = Voter("Joao")
    voter5 = Voter("Arthur")

    candidate1.add_observer(voter1)
    candidate2.add_observer(voter2)

    voter1.vote(candidate1)
    voter2.vote(candidate2)
    voter3.vote(candidate2)
    voter4.vote(candidate1)
    voter5.vote(candidate2)

    if (candidate1.votes > candidate2.votes):
        print("Candidate " + candidate1.name + " won!")
    elif (candidate1.votes == candidate2.votes):
        print("Draw")
    else:
        print("Candidate " + candidate2.name + " won!")
