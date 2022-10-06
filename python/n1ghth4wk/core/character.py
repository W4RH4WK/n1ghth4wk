from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Character:
    name: str

    strength: int = 2
    agility: int = 2
    logic: int = 2
    willpower: int = 2
    charisma: int = 2
    edge: int = 1
    edge_points: int = edge

    skill_ratings: Dict[str, int] = field(default_factory=dict)

    @property
    def perception(self):
        return self.logic + self.willpower

    def info(self):
        print(f'{self.name}')

        print('------------------------ Attributes')
        print(' S  A  L  W  C  E')
        print(f'{self.strength:2} {self.agility:2} {self.logic:2} {self.willpower:2} {self.charisma:2} {self.edge:2} ({self.edge_points})')

        print('------------------------ Skills')
        for skill, rating in self.skill_ratings.items():
            if rating > 0:
                print(f'{skill:>20}: {rating:2}')

    def __post_init__(self):
        from .skills import addDefaultSkillsToCharacter
        addDefaultSkillsToCharacter(self)

    def __str__(self):
        return self.name
