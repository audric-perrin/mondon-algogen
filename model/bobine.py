# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Bobine:
    def __init__(self, code: int, color: str, laize: float, longueur: int, poses: List[int]) -> None:
        self.code = code
        self.color = color
        self.laize = laize
        self.longueur = longueur
        self.poses = poses

    def __str__(self):
        return "B{}({}, {}, {}, {})".format(self.code, self.color.capitalize(), self.laize, self.longueur, self.poses)
