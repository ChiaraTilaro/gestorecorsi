from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDWithIscritti(self, pd):
        result = DAO.getCorsiPDWithIscritti(pd)
        result.sort(key= lambda s: s[1] , reverse=True)
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s:s.cognome)
        return studenti

    def getCDSOfCorso(self, codins):
        cds = DAO.getCDSOfCorso(codins)
        cds.sort(key=lambda  c: c[1] , reverse=True)
        return cds
