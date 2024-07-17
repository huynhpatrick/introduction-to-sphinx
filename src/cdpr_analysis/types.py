"""Subpackage for the types of required for the
analysis of Cable-Driven Parallel Robots.
"""

from typing import List


class Pose:
    """Class for a pose. A pose consists of a three-dimensional position vector
    and a 3x3 rotation matrix.

    :param position: Position vector
    :type position: List[float]
    :param orientation: Rotation matrix
    :type orientation: List[List[float]]
    """
    def __init__(self, position: List[float], orientation: List[List[float]]):
        """Constructor method

        :param position: Position vector
        :type position: List[float]
        :param orientation: Rotation matrix
        :type orientation: List[List[float]]
        """
        self.position = position
        self.orientation = orientation
