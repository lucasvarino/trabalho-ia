# Classe para representar os estados do problema da travessia da familia do rio
from member import Membro


class State:
    def __init__(self) -> None:
        self.left = [Membro.PAI, Membro.MAE,
                     Membro.FILHO, Membro.FILHO, Membro.BARCO]
        self.right = []

    def __str__(self) -> str:
        return f'Left: {self.left}\nRight: {self.right}'

    def apply_rule(self, rule) -> 'State':
        if rule.is_valid(self):
            new_state = State()
            new_state.left = self.left[:]
            new_state.right = self.right[:]
            rule.apply(new_state)
            # Substituir o estado atual pelo novo estado
            self.left = new_state.left[:]
            self.right = new_state.right[:]
            return new_state
        return None

    def is_complete(self) -> bool:
        return self.left == [] & self.right == [Membro.PAI, Membro.MAE, Membro.FILHO, Membro.FILHO, Membro.BARCO]
