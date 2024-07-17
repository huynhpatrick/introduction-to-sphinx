from cdpr_analysis.model import CableDrivenParallelRobot
from cdpr_analysis.types import Pose
from typing import List


class InverseKinematics:
    def __init__(self, cdpr: CableDrivenParallelRobot):
        self.cdpr = cdpr

    def calculate(self, pose: Pose) -> List[float]:
        print("calculating inverse kinematics")
        return [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
