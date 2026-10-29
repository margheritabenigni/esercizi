class Filosofo:
    def __init__(self, nome, anno):
        self.nome = nome
        self.anno = anno

    def caratteristiche(self):
        print("Nome:", self.nome)
        print("Anno:", self.anno)


class ScuolaFilosofica:
    def __init__(self, nome, fondatore, epoca, filosofi=[]):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        self.filosofi = filosofi.copy()

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)

    def stampa_filosofi(self):
        for filosofo in self.filosofi:
            filosofo.caratteristiche()

    def aggiungi_filosofo(self, filosofo):
        self.filosofi.append(filosofo)


class Platonismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi,
          valore_virtu_principale):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.valore_virtu_principale = valore_virtu_principale

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)
        print("Valore virtù principale:",
              self.valore_virtu_principale)


class Aristotelismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi,
                 obiettivo_principale):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.obiettivo_principale = obiettivo_principale

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)
        print("Obiettivo principale:", self.obiettivo_principale)


# Creazione dei filosofi
f1 = Filosofo("Platone", 125)
f2 = Filosofo("Aristotele", 240)
f3 = Filosofo("Pitagora", 315)
f4 = Filosofo("Socrate", 180)
f5 = Filosofo("Eraclito", 95)


# Creazione delle scuole filosofiche
platonismo = Platonismo(
    "Platonismo",
    "Platone",
    "Età classica",
    [f1, f4],
    "Giustizia"
)

aristotelismo = Aristotelismo(
    "Aristotelismo",
    "Aristotele",
    "Età classica",
    [f2],
    "Ricerca della felicità"
)


# Descrizione delle scuole
platonismo.descrivi()
aristotelismo.descrivi()


# Aggiunta di filosofi
platonismo.aggiungi_filosofo(f3)
aristotelismo.aggiungi_filosofo(f5)


# Stampa dei filosofi
platonismo.stampa_filosofi()
aristotelismo.stampa_filosofi()
