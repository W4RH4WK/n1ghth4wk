from typing import Callable

from .character import Character
from .checks import CheckBuilder


def addSkillToCharacter(c: Character, skill: Callable[[Character], int], rating: int = 0):
    c.skill_ratings[skill.__name__] = rating
    setattr(c, skill.__name__, lambda: CheckBuilder(skill(c)))


def addDefaultSkillsToCharacter(c: Character):
    addSkillToCharacter(c, athletics)
    addSkillToCharacter(c, closeCombat)
    addSkillToCharacter(c, projectileWeapons)
    addSkillToCharacter(c, firearms)
    addSkillToCharacter(c, heavyWeapons)
    addSkillToCharacter(c, vehicleWeapons)
    addSkillToCharacter(c, stealth)
    addSkillToCharacter(c, escapeArtist)
    addSkillToCharacter(c, pilotGroundcraft)
    addSkillToCharacter(c, pilotDrone)
    addSkillToCharacter(c, survival)
    addSkillToCharacter(c, biotech)
    addSkillToCharacter(c, electronics)
    addSkillToCharacter(c, engineering)
    addSkillToCharacter(c, tracking)
    addSkillToCharacter(c, con)
    addSkillToCharacter(c, intimidation)
    addSkillToCharacter(c, negotiation)
    addSkillToCharacter(c, disguise)


def addHackingSkillsToCharacter(c: Character):
    addSkillToCharacter(c, hacking)


def addTechnomancerSkillsToCharacter(c: Character):
    addSkillToCharacter(c, hacking)
    addSkillToCharacter(c, tasking)


def addMagicSkillsToCharacter(c: Character):
    addSkillToCharacter(c, sorcery)
    addSkillToCharacter(c, conjuring)
    addSkillToCharacter(c, astralCombat)


# Strength Skills

def athletics(c: Character) -> int:
    return c.strength + c.skill_ratings.get('athletics', 0)


# Agility Skills

def closeCombat(c:Character) -> int:
    return c.agility + c.skill_ratings.get('closeCombat', 0)


def projectileWeapons(c:Character) -> int:
    return c.agility + c.skill_ratings.get('projectileWeapons', 0)


def firearms(c:Character) -> int:
    return c.agility + c.skill_ratings.get('firearms', 0)


def heavyWeapons(c:Character) -> int:
    return c.agility + c.skill_ratings.get('heavyWeapons', 0)


def vehicleWeapons(c:Character) -> int:
    return c.agility + c.skill_ratings.get('vehicleWeapons', 0)


def stealth(c:Character) -> int:
    return c.agility + c.skill_ratings.get('stealth', 0)


def escapeArtist(c:Character) -> int:
    return c.agility + c.skill_ratings.get('escapeArtist', 0)


def pilotGroundcraft(c:Character) -> int:
    return c.agility + c.skill_ratings.get('pilotGroundcraft', 0)


def pilotDrone(c:Character) -> int:
    return c.agility + c.skill_ratings.get('pilotDrone', 0)


def pilotAircraft(c:Character) -> int:
    return c.agility + c.skill_ratings.get('pilotAircraft', 0)


def pilotWatercraft(c:Character) -> int:
    return c.agility + c.skill_ratings.get('pilotWatercraft', 0)


# Willpower Skill

def sorcery(c: Character) -> int:
    return c.willpower + c.skill_ratings.get('sorcery', 0)


def conjuring(c: Character) -> int:
    return c.willpower + c.skill_ratings.get('conjuring', 0)


def astralCombat(c: Character) -> int:
    return c.willpower + c.skill_ratings.get('astralCombat', 0)


def survival(c: Character) -> int:
    return c.willpower + c.skill_ratings.get('survival', 0)


# Logic Skill

def biotech(c: Character) -> int:
    return c.logic + c.skill_ratings.get('biotech', 0)


def hacking(c: Character) -> int:
    return c.logic + c.skill_ratings.get('hacking', 0)


def electronics(c: Character) -> int:
    return c.logic + c.skill_ratings.get('electronics', 0)


def engineering(c: Character) -> int:
    return c.logic + c.skill_ratings.get('engineering', 0)


def tracking(c: Character) -> int:
    return c.logic + c.skill_ratings.get('tracking', 0)


def tasking(c: Character) -> int:
    return c.logic + c.skill_ratings.get('tasking', 0)


# Charisma Skills

def con(c: Character) -> int:
    return c.charisma + c.skill_ratings.get('con', 0)


def intimidation(c: Character) -> int:
    return c.charisma + c.skill_ratings.get('intimidation', 0)


def negotiation(c: Character) -> int:
    return c.charisma + c.skill_ratings.get('negotiation', 0)


def disguise(c: Character) -> int:
    return c.charisma + c.skill_ratings.get('disguise', 0)
