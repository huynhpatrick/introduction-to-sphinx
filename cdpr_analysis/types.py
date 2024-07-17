from typing import List


class Pose:
    def __init__(self, position: List[float], orientation: List[List[float]]):
        self.position = position
        self.orientation = orientation
