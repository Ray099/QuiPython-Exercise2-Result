class Finance:
    def __init__(self):
        self.totalList = []
        self.totalMoney = 0

    def currentCash(self):
        self.totalMoney = Income.addIn(self) - Outcome.addOut(self)
        return self.totalMoney

    def getAllMovements(self):
        self.totalList.append(Income.getAllIns(self))
        self.totalList.append(Outcome.getAllOuts(self))
        return self.totalList


class Income:
    def __init__(self):
        self.inList = []
        self.inMoney = 0

    def addIn(self):
        self.inMoney += int(input("inserte la cantidad que quiere ingresar: "))
        self.inList.append(self.inMoney)
        return self.inMoney

    def getAllIns(self):
        return print(self.inList)


class Outcome:
    def __init__(self):
        self.outList = []
        self.outMoney = 0

    def addOut(self):
        self.outMoney += int(input("inserte la cantidad que quiere egresar: "))
        self.outList.append(self.outMoney)
        return self.outMoney

    def getAllOuts(self):
        return print(self.outList)
