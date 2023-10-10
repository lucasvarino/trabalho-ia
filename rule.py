import state as st
from member import Membro
from enum import Enum


class Rule:
    boat = []

    def __init__(self, first, second) -> None:
        self.boat.append(first)
        self.boat.append(second)

    def is_valid(self, state: st.State) -> bool:
        # Fazer as verificações das regras

        # Se houver dois adultos no barco, não é valido
        if sum(1 for valor in self.boat if valor in {Membro.PAI, Membro.MAE}) >= 2:
            return False

        # Se houver mais de 2 pessoas no barco, não é valido (barco + 2 pessoas)
        if len(self.boat) > 3:
            return False

        return True
