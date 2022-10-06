class Attribute:
    def __init__(self, label: str, score: int):
        self.label = label
        self.score = score

    def __int__(self):
        return self.score

    def __str__(self):
        return f'{self.label}: {self.score}'


class Strength(Attribute):
    def __init__(self, score: int):
        super(Strength, self).__init__('S', score)


class Agility(Attribute):
    def __init__(self, score: int):
        super(Agility, self).__init__('A', score)


class Logic(Attribute):
    def __init__(self, score: int):
        super(Logic, self).__init__('L', score)


class Willpower(Attribute):
    def __init__(self, score: int):
        super(Willpower, self).__init__('W', score)


class Charisma(Attribute):
    def __init__(self, score: int):
        super(Charisma, self).__init__('C', score)


class Edge(Attribute):
    def __init__(self, score: int):
        super(Edge, self).__init__('E', score)

