class CableDrivenParallelRobot:
    def __init__(self, name: str):
        self.name: str = name

    def saveXml(self, filepath: str):
        print("saving " + filepath)

    @staticmethod
    def loadXml(filepath: str):
        print("loading " + filepath)
        return CableDrivenParallelRobot(filepath)
