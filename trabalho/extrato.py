from datetime import date
import os, io

class Extrato:
    def __init__(self):
        self._extrato = []

    @property
    def extrato(self):
        return self._extrato

    def imprimir(self, numero):
        today = date.today()
        day = today.strftime("%d_%m_%Y")
        dir = os.path.dirname(__file__)
        with io.open(f'{dir}\extratos\conta_{numero}_{day}.txt','a', encoding="utf-8") as logger:
            for mov in self.extrato:
                logger.write(f"{mov}\n")