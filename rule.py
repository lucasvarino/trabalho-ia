import state as st
from member import Membro
from enum import Enum


class Rule:

    def __init__(self, direction, first, second=None) -> None:
        self.boat = []
        self.direction = direction
        self.boat.append(first)
        if second is not None:
            self.boat.append(second)

        self.boat.append(Membro.BARCO)

    def is_valid(self, state: st.State) -> bool:
        # Fazer as verificações das regras

        # Se houver dois adultos no barco, não é valido
        if sum(1 for valor in self.boat if valor in {Membro.PAI, Membro.MAE}) >= 2:
            return False

        # Se houver mais de 2 pessoas no barco, não é valido (barco + 2 pessoas)
        if len(self.boat) > 3:
            return False

        return True

    def apply(self, state: st.State):
        # Tirar os membros do barco do lado que estão
        for member in self.boat:
            if self.direction == 0:
                if member in state.left:
                    state.left.remove(member)
                    state.right.append(member)
            else:
                if member in state.right:
                    state.right.remove(member)
                    state.left.append(member)
