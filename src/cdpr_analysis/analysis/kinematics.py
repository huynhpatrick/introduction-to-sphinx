"""Subpackage for the kinematics analysis of
a Cable-Driven Parallel Robot.
"""

from cdpr_analysis.model import CableDrivenParallelRobot
from cdpr_analysis.types import Pose
from typing import List


class ForwardKinematics:
    """Class for the forward kinematics calculation of a Cable-Driven Parallel Robot.

    :param cdpr: The Cable-Driven Parallel Robot to be analyzed
    :type cdpr: :class: `cdpr_analysis.model.CableDrivenParallelRobot`
    """
    def __init__(self, cdpr: CableDrivenParallelRobot):
        """Constructor method

        :param cdpr: The Cable-Driven Parallel Robot to be analyzed
        :type cdpr: :class: `cdpr_analysis.model.CableDrivenParallelRobot`
        """
        self.cdpr = cdpr

    def calculate(self, cable_lengths: List[float]) -> Pose:
        """Calculates the forward kinematics pose of a Cable-Driven Robot.

        :param cable_lengths: Lengths of the cables
        :type cable_lengths: List[float]
        :return: The pose
        :rtype: :class:`Pose`
        """
        print("calculating forward kinematics")
        return Pose([0.0, 0.0, 0.0], [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])


class InverseKinematics:
    """Class for the inverse kinematics calculation of a Cable-Driven Parallel Robot.

    :param cdpr: The Cable-Driven Parallel Robot to be analyzed
    :type cdpr: :class: `cdpr_analysis.model.CableDrivenParallelRobot`
    """
    def __init__(self, cdpr: CableDrivenParallelRobot):
        self.cdpr = cdpr

    def calculate(self, pose: Pose) -> List[float]:
        """
        Calculates the inverse kinematics pose of a Cable-Driven Robot.

        :param pose: The pose of the Cable-Driven Parallel Robot
        :type pose: :class:`cdpr_analysis.types.Pose`
        :return: cable lengths
        :rtype: List[float]
        """
        print("calculating inverse kinematics")
        return [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
