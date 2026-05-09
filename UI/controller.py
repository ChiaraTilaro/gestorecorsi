import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value

        if pd == None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)
        if not len(corsiPD):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico")
            )
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
                ft.Text(f"Di seguito i corsi del {pd} periodo didattico")
            )
        for c in corsiPD:
            self._view.txt_result.controls.append(
                ft.Text(c)
            )
        self._view.update_page()




    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value

        if pd == None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPD = self._model.getCorsiPDWithIscritti(pdInt)
        if not len(corsiPD):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico")
            )
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
                ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti")
            )
        for c in corsiPD:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]}-- N iscritti: {c[1]}")
            )
        self._view.update_page()


    def handlePrintIscrittiCodins(self , e):
        self._view.txt_result.controls.clear()
        codins = self._view.ddCodins.value
        if codins is None:
            self._view.create_alert("Per favore selezionare un insegnamento")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(codins)

        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text("Nessuno studente iscritto a questo corso")
            )
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue}")
        )
        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(s)
            )
        self._view.update_page()



    def handlePrintCDSCodins(self , e):
        self._view.txt_result.controls.clear()
        codins = self._view.ddCodins.value
        if codins is None:
            self._view.create_alert("Per favore selezionare un insegnamento")
            self._view.update_page()
            return
        cds = self._model.getCDSOfCorso(codins)

        if not len(cds):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun CDS afferente al corso {codins}")
            )
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i CDS che frequentano il corso {codins}")
        )
        for c in cds:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} - N iscritti: {c[1]}")
            )
        self._view.update_page()


    def fillddCodins(self):
        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(
                ft.dropdown.Option(key=c.codins,
                                   data= c,
                                   on_click= self._choiseDDCodins)
            )

    def _choiseDDCodins(self , e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)


