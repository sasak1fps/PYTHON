class assesment:
    def __init__(self, name, subject , score = 0):
        self.name = name
        self.subject = subject
        self._score = score

    def get_score(self):
        return print(f"{self.name} got {self._score} in {self.subject}")
    def set_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError("Score must be between 0 and 100") 

av1 = assesment("John", "Maths")
av1.set_score(50)
av1.get_score()

class assesment2:
    def __init__(self, name, subject , score = 0):
        self.name = name
        self.subject = subject
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError("Score must be between 0 and 100")

av2 = assesment2("John", "Maths")
av2.score = 50
print(av2.score)