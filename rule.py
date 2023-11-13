import state as st
from member import Membro
from enum import Enum


class Rule:

    def __init__(self, first, second=None) -> None:
        self.boat = [] 
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
        # Verificar se o barco está do lado direito ou esquerdo
        if Membro.BARCO in state.left:
            # Remover os membros do barco do lado esquerdo
            for membro in self.boat:
                state.left.remove(membro)
                state.right.append(membro)
        else:
            # Remover os membros do barco do lado direito
            for membro in self.boat:
                state.right.remove(membro)
                state.left.append(membro)
