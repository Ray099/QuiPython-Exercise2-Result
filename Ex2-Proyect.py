from inner import Finance
from inner import Income
from inner import Outcome

print("Iniciar Finance EX2...")

finance = Finance()
income = Income()
outcome = Outcome()


def iniciarPrograma():
    startMsg = str("Se da inicio al programa Finace EX2")
    finance.__init__()
    income.__init__()
    outcome.__init__()

    return startMsg


def agregarIngreso():
    addI = income.addIn()
    return addI


def agregarEgreso():
    addE = outcome.addOut()
    return addE


def checkMoney():
    reportT = finance.currentCash()
    return reportT


def reportIncome():
    reportI = income.getAllIns()
    return reportI


def reportOutcome():
    reportO = outcome.getAllOuts()
    return reportO


def reportTransact():
    allList = finance.getAllMovements()
    return allList


def reportAccount():
    accountCheckUp = finance.currentCash()
    return accountCheckUp


while True:
    print("Menu: \n")
    print("(0) salir")
    print("(1) iniciar sistema ")
    print("(2) agregar ingresos ")
    print("(3) agregar egresos ")
    print("(4) chequear cantidad(es) actual(es) ")
    print("(5) generar reporte de ingresos ")
    print("(6) generar reporte de egresos ")
    print("(7) generar reporte de transacciones ")
    print("(8) generar reporte de toda la cuenta ")
    comando = int(input("presiona un numero para selecionar la opcion apropiada: "))

    if comando == 0:
        print("Hasta la proxima veeeeeezzz....\n")
        break

    elif comando == 1:
        iniciarPrograma()
        print("Se da inicio al programa Finace EX2")

    elif comando == 2:
        agregarIngreso()

    elif comando == 3:
        agregarEgreso()

    elif comando == 4:
        checkMoney()

    elif comando == 5:
        reportIncome()

    elif comando == 6:
        reportOutcome()

    elif comando == 7:
        print(
            "la lista entera de transacciones en su cuenta se ve de esta manera [Ingresos],[Egresos]"
        )
        reportTransact()

    elif comando == 8:
        print("la cantidad actual de dinero en su cuenta es...")
        reportAccount()
