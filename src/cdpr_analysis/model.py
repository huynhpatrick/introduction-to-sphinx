class CableDrivenParallelRobot:
    """A class which models a Cable-Driven Parallel Robot.

    :param name: The name of the Cable-Driven Parallel Robot
    :type name: str
    """
    def __init__(self, name: str):
        """Constructor method

        :param name: The name of the Cable-Driven Parallel Robot
        :type name: str
        """
        self.name: str = name

    def saveXml(self, filepath: str):
        """Saves the Cable-Driven Parallel Robot to a .xml file.

        :param filepath: The filepath of the file to be saved
        :type filepath: str
        """
        print("saving " + filepath)

    @staticmethod
    def loadXml(filepath: str):
        """Loads the Cable-Driven Parallel Robot from a .xml file.

        :param filepath: The filepath of the file to be loaded
        :type filepath: str
        :return: The loaded Cable-Driven Parallel Robot
        :rtype: class:`cdpr_analysis.model.CableDrivenParallelRobot`
        """
        print("loading " + filepath)
        return CableDrivenParallelRobot(filepath)
