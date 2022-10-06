from __future__ import annotations

import random

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


setSeed = random.seed
"""
Allows one to set a specific seed for the random number generator (RNG).
This allows rolls to be reproducible.
"""

verbose_checks = True
"""Enabling this option shows the result of dice rolls."""


class Glitch(Enum):
    NoGlitch = 0
    Glitch = 1
    CriticalGlitch = 2


def roll(num_dice: int, edge: bool = False, prefix: Optional[str] = None) -> Tuple[int, Glitch]:
    """Returns the number of Hits and whether its a Glitch."""
    if edge:
        num_dice += 1

    rolls = [random.randint(1,6) for _ in range(num_dice)]

    hits = rolls.count(5) + rolls.count(6)

    if edge:
        hits += rolls.count(4)

    ones = rolls.count(1)
    if ones > num_dice / 2:
        if hits == 0:
            glitch = Glitch.CriticalGlitch
        else:
            glitch = Glitch.Glitch
    else:
        glitch = Glitch.NoGlitch

    if verbose_checks:
        if prefix:
            print(f'{prefix}: ', end='')
        print(f'{hits:3} Hits | {glitch.name:14} {rolls}')

    return hits, glitch


def checkThreshold(num_dice: int, threshold: int, edge: bool = False) -> Tuple[bool, int, Glitch]:
    """Returns whether the check succeeded, the Net Hits, and whether it's a Glitch."""
    hits, glitch = roll(num_dice, edge=edge)
    return hits >= threshold, hits - threshold, glitch


def checkOpposed(num_dice: int, num_dice_opposed: int,
                 edge: bool = False, edge_opposed: bool = False) -> Tuple[bool, int, Glitch]:
    """Returns whether the check succeeded, the Net Hits, and whether it's a Glitch."""
    hits, glitch = roll(num_dice, edge=edge, prefix="Attacker")
    opposed_hits, _ = roll(num_dice_opposed, edge=edge_opposed, prefix="Defender")
    return hits >= opposed_hits, hits - opposed_hits, glitch


@dataclass
class CheckExtendedResult:
    success: bool = False
    threshold_left: int = 0
    intervals_spent: int = 0
    glitch: Glitch = Glitch.NoGlitch


def checkExtended(num_dice: int, threshold: int, max_intervals: Optional[int] = None,
                  edge: bool = False) -> CheckExtendedResult:
    """Returns whether the check succeeded, the number of intervals spent, and whether it's a Glitch."""
    state = CheckExtendedResult()
    state.success = True
    state.threshold_left = threshold
    state.intervals_spent = 0
    state.glitch = Glitch.NoGlitch

    while state.threshold_left > 0 and num_dice > 0:
        if max_intervals and state.intervals_spent >= max_intervals:
            return state

        hits, glitch = roll(num_dice, edge=edge)
        state.intervals_spent += 1

        # Edge is only used for the first roll.
        edge = False

        # CriticalGlitch can only occur on the first roll.
        if state.intervals_spent == 1 and glitch == Glitch.CriticalGlitch:
            state.glitch = Glitch.CriticalGlitch
            return state

        # A Glitch nullifies all hits of the current roll.
        if glitch == Glitch.Glitch:
            hits = 0

        state.threshold_left -= hits
        state.success = state.threshold_left <= 0

        num_dice -= 1
    return state


class CheckBuilder:
    def __init__(self, num_dice: int):
        self.num_dice = num_dice
        self.edge = False

    def edge(self) -> CheckBuilder:
        self.edge = True
        return self

    def modifier(self, modifier: int) -> CheckBuilder:
        self.num_dice += modifier
        self.num_dice = max(0, self.num_dice)
        return self

    def roll(self) -> Tuple[int, Glitch]:
        return roll(self.num_dice, self.edge)

    def checkThreshold(self, threshold: int) -> Tuple[bool, int, Glitch]:
        return checkThreshold(self.num_dice, threshold, self.edge)
