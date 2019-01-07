#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List


Vector = List[float]
# create a test type 


def scale(scalar: float, vector: Vector) -> Vector:
    vector.append(34)
    vector[3].hex()
    # autocomplete success

    return [scalar * num for num in vector]

from typing import NewType




