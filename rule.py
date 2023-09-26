import state as st
from member import Membro, Adulto
from enum import Enum


class Rule:
    boat = []

    def __init__(self, first, second) -> None:
        self.boat.append(first)
        self.boat.append(second)

    def is_valid(self, state: st.State) -> bool:
        # Fazer as verificações das regras

        # Se houver dois adultos no barco, não é valido
        if sum(1 for valor in self.boat if valor in {Adulto.PAI, Adulto.MAE}) >= 2:
            return False

        # Se houver mais de 2 pessoas no barco, não é valido
        if len(self.boat) > 2:
            return False

        return True
